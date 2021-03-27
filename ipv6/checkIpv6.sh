#!/bin/bash

#获取完整的ipv6的地址格式（用空格代替冒号）
function complete_Ipv6()
{
 local IPV6=$1
 # IPV6地址格式的冒号数
 num=`(echo $IPV6 | grep -o ":" |wc -l)`
 echo $IPV6 > /home/FusionAccess/ipv6.tem
 while [ $num -lt 6 ]; do
   sed -i "s/::/:0000::/g" /home/FusionAccess/ipv6.tem
   let num++
 done
 if [ $num -eq 6 ]
 then
 sed -i "s/::/:0000:0000:/g" /home/FusionAccess/ipv6.tem
 fi
 ipv6str=`cat /home/FusionAccess/ipv6.tem`
 # 用空格代替冒号
 ipv6str=${ipv6str//:/ }
 rm -rf /home/FusionAccess/ipv6.tem
 echo ${ipv6}
}

# 获取16位的二进制
function Binary_length()
{
  local num=$1
  # 将小写转化为大写
  array=`echo ${num}|tr '[a-z]' '[A-Z]'`
  # 十六进制转化为二进制
  Binary=`echo "ibase=16;obase=2;${array}"|bc`
  Binary_length=(${Binary})
  # 获取二进制的长度
  length=${#Binary_length}
  value=16-${length}
  # 若是不足16位则补零
  j=0
  while [[ j -lt ${value}]];do
    result+=0
    let j++
  done
  echo "${result}${Binary}"
}

# 获取二进制
function binary()
{
 for num in $array
 do
   echo $(Binary_length ${num})
 done
}

#获取ipv6的128位的二进制和前缀
function prefixlen()
{
  local ipv6=$1
  local prefixlen=$2
  # 小写转化为大写
  array=`echo $(complete_Ipv6 ${ipv6})|tr '[a-z]' '[A-Z]'`
  # 获取二进制的长度并删除空格
  Binary_all_length=`echo $(binary ${array}|sed 's/ //g')`
  # 获取128位的二进制的长度并删除空格
  result=$(echo ${Binary_all_length}|tr -d ' ')
  # 获取前缀
  prefixlen=$(echo ${result[*]:0:${prefixlen}})
  echo ${prefixlen}
}
prefixlen "1a2b::e572:f0c1:3e1b:3ecc" "10"


function foo()
{
 local IPV6=$1
 echo $IPV6 > /home/FusionAccess/ipv6.tem
 ipv6str=`cat /home/FusionAccess/ipv6.tem`
 str=${ipv6str//:/ }
 rm -rf /home/FusionAccess/ipv6.tem
 arr=($str)
 i=0
 while [[ i -lt ${#arr[@]}]];
 do
   arr[i]=`(echo ${arr[i]}|awk '{print strtonum("0x"$0)}'|awk '{printf("%04x\n",$0)}')`
   let i++
 done
 ipv6=$(echo ${arr[@]}|sed 's/ //g')
 echo "ipv6:${ipv6}"
}

# 检查ipv6的格式
function checkIpv6()
{
  local IP=$1
  # 获取前缀并判断前缀是否为空或大于128
  prefixlen=`(echo $Ip |awk -F '/' '{print $2}')`
  if [[ "$prefixlen" == "" ]];then
    return 1
  elif [[ $prefixlen -gt 128 ]];then
    return 1
  fi
  ipv6=`(echo $Ip |awk -F '/' '{print $1}')`
  num=`(echo $ipv6 |grep -o ":" | wc -l )`
  if [ $num -gt 8 ];then
    return 1
  fi
  str=`(echo ${ipv6//:/})`
  # 比较ipv6的地址的每一个数小于f
  i=0
  while [[ i -lt ${#str} ]];do
    local char=`echo ${str:i:1}`
    if [[ ${char} > "f" ]];then
      return 1
    fi
    let i++
  done
  # 以空格切割，比较ipv6的每段长度是否大于4
  arr=(${ipv6//:/ })
  for var in ${arr[@]}
  do
    if [[ 4 < ${#arr} ]];then
      return 1
    fi
  done
  return 0
}