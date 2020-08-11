#day24
#1.将一个文件从客户端发送到服务端,要求文件类型随意
from socket import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

c,addr = s.accept()
print("Connect from",addr)

# 以二进制写入
f = open('mm.jpg','wb')

#循环接收内容,写入文件
while True:
  data = c.recv(1024)
  if data == b'##':
    break
  f.write(data)

data = c.recv(1024)
print(data.decode())

f.close()
c.close()
s.close()

from socket import *
import time

s = socket()
s.connect(('127.0.0.1',8888))

f = open('img.jpg','rb')

# 读取内容,将其发送
while True:
  data = f.read(1024)
  if not data:
    time.sleep(0.1)
    s.send(b'##')
    break
  s.send(data)

time.sleep(0.1)
s.send("发送完毕".encode())

f.close()
s.close()

#2.将tcp的俩个程序和函数熟练掌握
"""
1.网络基础编程
2.os模型(tcp/ip模型)
tcp udp的区别
三次握手,四次挥手

面试技巧:这是什么,干什么用,我用它干什么,往自己熟悉的方向引导面试官
3.套接字编程
tcp套接字
udp套接字
4.tcp服务端
tcp客户端
"""