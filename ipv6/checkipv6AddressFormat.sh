#!/bin/bash
function checkipv6AddressFormat()
{
  local Ip=$1
  # ::/128,即0:0:0:0:0:0:0:0,只能作为尚未获取正式地址的主机源地址，不能作为目的地址，不能分配给真实的网络接口
  if [[ "$Ip" == "::/128" ]];then
    return 1
  fi
  # can not be ::/128,即0:0:0:0:0:0:0:1，回环地址，相当于IPV4中的localhost的127.0.0.1
  if [[ "$Ip" == "::1/128" ]];then
    return 1
  fi
  # can not be FC::/7,本地站点地址，类似于IPV4私有地址，本地站点地址不会与全球IPV6通信
  # FC::10已被废弃，目前新的地址为FC::/7
  if [[ "$Ip" == "FC::/7" ]];then
    return 1
  fi
  # can not be fe80::/10，本地链路地址，用于单一链路，适用于自动配置、邻机发现等，路由器不转发以fe80开头的地址
  if [[ "$Ip" == "fe80::/10" ]];then
    return 1
  fi
  # 不支持以：开头的压缩格式
  if [[ "$Ip" == ":.*" ]];then
    return 1
  fi
  prefixlen=`(echo $Ip |awk -F '/' '{print $2}')`
  if [[ "$prefixlen" == "" ]];then
    return 1
  elif [[ $prefixlen -gt 128 ]];then
    return 1
  fi
  local IPV6=$Ip
  num=`(echo $IPV6| grep -o ":"|wc -l)`
  ipv6=`(echo $IPV6 |awk -F '/' '{print $1}')`
  echo $ipv6 > /home/FusionAccess/ipv6.tem
  while [ $num -lt 6];do
    sed -i "s/::/:0000::/g" /home/FusionAccess/ipv6.tem
    let num++
  done
  if [ $num -eq 6];then
    sed -i "s/::/:0000:0000:/g" /home/FusionAccess/ipv6.tem
  fi
  ipv6str=`cat /home/FusionAccess/ipv6.tem`
  str=${ipv6//:/ }
  rm -rf /home/FusionAccess/ipv6.tem
  arr=($str)
  i=0
  while [[ i -lt ${#arr[@]}]];do
    arr[i]=`(echo ${arr[i]} | awk '{print strtonum("0x"$0)}' | awk '{printf("%04x/n",$0)}')`
    let i++
  done
  array=$(echo ${arr[@]})
  for num in $array
    value=${num}
    if [[ $value -gt 65535]] || [[ $value -lt 0 ]];then
      return 1
    fi
  done
  return 0
}
#input and check IP address
#param:
#1-displayTips display tips to user
#2-checkCollect:0 IP can not be used,1 IP must be collect,2 not check collection
function inputAndCheckIpv6Address()
{
  local displayTips=$1
  local checkCollect=$2
  while:
  do
    read -t 36000 -e -p "${displayTips}" input_ip_address
    if [ "x$input_ip_address" == "xq"] -o [ "x$input_ip_address" == "xQ"];then
      echo -e "\033[31mYou have chosen back\033[1m"
      return 9
    fi
    if [ "x$input_ip_address" == "xskip"] -o [ "x$input_ip_address" == "xSKIP"];then
      echo -e "\033[31mYou have chosen skip\033[1m"
      return 8
    fi
    checkipv6AddressFormat $input_ip_address
    result=$?
    if [ result -ne 0 ];then
      echo -e "\033[31mIncorrect IPV6 Address\033[1m"
      continue
    fi
    if [ $checkCollect -eq 0];then
      checkIpv6Reachable $input_ip_address
      if [ $? -eq 0 ];then
        echo -e "\033[31mIp has been used,please retry.\033[1m"
        continue
      else
        break
      fi
    elif [ $checkCollect -eq 1];then
      checkIpv6Reachable $input_ip_address
      if [ $? -ne 0 ];then
        echo -e "\033[31mFailed to connet to the IP address,please enter a correct IP address.\033[1m"
        continue
      else
        break
      fi
    else
      break
    fi
  done
  return 0
}

#拉起ipv4的网卡
ifconfig $floatPort $floatIp netmask $mask up
arping -w 1 -A -I $floatPort $floatIp
if [ $? -ne 0 ];then
  device=`(echo $floatPort | awk -F ':' '{print $1}')`
  arping -w 1 -A -I $device $floatIp
fi
#拉起ipv6的网卡
ifconfig $floatPort inet6 add $floatIpv6 up
ping -6 -c 1 -w 1 $floatIpv6
if [ $? -ne 0 ];then
  floatipv6=`(echo $floatIpv6 | awk -F '/' '{print $1}')`
  ping -6 -c 1 -w 1 $floatipv6
fi


if [ ! -e /etc/EulerLinux.conf ];then
  devList=`ifconfig | grep eth | awk -F ' ' '{print $1}'`
  for dev in $devList
  do
    ind=`expr index $dev ':'`
    if [ $ind -eq 0 ];then
      dev_ip=`ifconfig $dev| grep "inet addr" |awk -F "inet addr:" "{print $2}"| awk -F " " "{print $1}"`
      dev_mask=`ifconfig $dev |grep "inet addr"|awk -F "Mask:" "{print $2}"`
      dev_network=`get_network $dev_ip $dev_mask`
      if [ "$dev_network" == "$input_network" ];then
        log "match network is found:$dev $dev_ip $dev_mask"
        flag=true
        DEVICE=$dev:1
        break 
      fi
    fi
  done
else
  dev_List=`cd /etc/sysconfig/network-scripts/ && ls ifcfg-* | grep -v ifcfg-lo |awk -F '-' '{print $2}'`
  for dev in $dev_List
  do
    dev_ip=`ifconfig $dev |grep -i "inet "| grep -v 127.0.0.1| awk -F " " "{print $2}" |tr -d " "`
    dev_mask=`ifconfig $dev |grep -i "netmask "| grep -v 127.0.0.1| awk -F " " "{print $4}" |tr -d " "`
    dev_network=`get_network $dev_ip $dev_mask`
      if [ "$dev_network" == "$input_network" ];then
        log "match network is found:$dev $dev_ip $dev_mask"
        flag=true
        DEVICE=$dev:1
        break
      fi
    fi
  done
fi

# 添加IPV6地址
ip -6 addr add <ipv6address>/<prefixlength> dev <interface>
ip -6 addr add 2001:0db8:0:f101::1/64 dev eth0

ifconfig <interface> inet6 add <ipv6address>/<prefixlength>
ifconfig eth0 inet6 add 2001:0db8:0:f101::1/64

# 添加默认路由
ip -6 route add <ipv6network>/<prefixlength> via <ipv6address>
ip -6 route add default via 2001:0db8:0:f101::1

route -A inet6 add <ipv6network>/<prefixlength> gw
route -A inet6 add default gw 2001:0db8:0:f101::1

# 查看路由
ip -6 route show
route -A 'inet6'
route -6

# windows查看路由表
route print

# 查看邻居缓存
ip -6 neighbor show

# windows查看邻居缓存
netsh interface ipv6 show neighbors

