#<计算机原理>和<编程原理>
#day23
#1.文件函数使用熟练(open,read,write)
#2.从终端输入一个文件名称(包含路径),\
#  如果该文件存在则将该文件复制到当前目录下,\
#  命名1904(要求文件可以使任意类型),\
#  如果文件不存在则打印该文件不存在
#　输入文件名
filename = input("File:")

try:
  fr = open(filename,'rb')
except FileNotFoundError as e:
  print(e)
else:
  fw = open('file.jpg','wb')

  #　循环复制
  while True:
    data = fr.read(1024)
    if not data:
      break
    fw.write(data)

  fr.close()
  fw.close()
#3.向一个文件写入日志,写入格式:
#   1. 2019-1-1 12:12:23
#要求:每隔一秒写入一次,每条时间占一行,程序死循环,ctrl-c退出重新启动
import time
f=open("log.txt","a+")
n=0
f.seek(0,0)#将偏移量移动待开始计数
for line in f:
    n+=1
while True:
    n+=1
    time.sleep(1)
    s="%d. %s\n"%(n,time.ctime())
    f.write(s)
    f.flush()#随时看到文件变化


"""
day23
字符串---->python中表示二进制的一种形式
b"*****"
字符串-->字节串　　　str.encode()
字节串-->字符串　　　bytes.decode()
文件操作:
open()     close()
read()     readline()    readlines()
write()    writelines()
r     读      文件必须存在
w     写      文件不存在时创建文件　文件存在时则清空
a     追加    文件不存在时创建文件　文件存在时则追加
+           　对原有权限加成
b             以二进制形式打开
细节处理
缓冲区　flush()
文件偏移量   tell()  seek()
文件描述符   fileno()
4. 文件处理接口   os
"""
