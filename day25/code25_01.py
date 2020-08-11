"""
tcp粘包问题
"""
import socket
sockfd = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)
sockfd.bind(('0.0.0.0', 8888))
sockfd.listen(3)
while True:
  print("Waiting for connect ...")
  connfd, addr = sockfd.accept()
  print("Connect from", addr)
  n = 0
  while n < 10:
    n += 1
    data = connfd.recv(5)
    print(data)
  connfd.close()  # 断开连接
#　关闭套接字
sockfd.close()

#udp套接字客户端流程
from socket import *
#服务端地址
ADDR=("176.140.10.215",8888)
#创建数据字套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
#循环发送消息
while True:
    data=input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr=sockfd.recvfrom(1024)
    print("From server:",addr)
#关闭套接字
sockfd.close()

"""
udp客户端流程
重点代码
"""
from socket import *
# 服务端地址
ADDR = ('176.140.10.215',8888)
# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
# 循环发送消息
while True:
  data = input("Word>>")
  if not data:
    break
  sockfd.sendto(data.encode(),ADDR)
  msg,addr = sockfd.recvfrom(1024)
  print("From server:",msg.decode())
sockfd.close()


