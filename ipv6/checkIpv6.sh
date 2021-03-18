#!/bin/bash

#获取完整的ipv6的地址格式（用空格代替冒号）
function complete_Ipv6()
{
 local IPV6=$1
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
 ipv6str=${ipv6str//:/ }
 rm -rf /home/FusionAccess/ipv6.tem
 echo ${ipv6}
}

# 获取16位的二进制
function Binary_length()
{
  local num=$1
  array=`echo ${num}|tr '[a-z]' '[A-Z]'`
  Binary=`echo "ibase=16;obase=2;${array}"|bc`
  Binary_length=(${Binary})
  length=${#Binary_length}
  value=16-${length}
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
  array=`echo $(complete_Ipv6 ${ipv6})|tr '[a-z]' '[A-Z]'`
  Binary_all_length=`echo $(binary ${array}|sed 's/ //g')`
  result=$(echo ${Binary_all_length}|tr -d ' ')
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
 while [[ i -lt ${#arr[@]}]];do
   arr[i]=`(echo ${arr[i]}|awk '{print strtonum("0x"$0)}'|awk '{printf("%04x\n",$0)}')`
   let i++
   done
   ipv6=$(echo ${arr[@]}|sed 's/ //g')
   echo "ipv6:${ipv6}"
}






