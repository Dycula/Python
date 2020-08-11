"""
tcp客户端流程
"""
from socket import *

#1.创建流式套接字
sockfd=socket() #参数默认即tcp套接字

#2.连接服务端程序
server_addr=("176.140.10.215",8888)#服务端地址
sockfd.connect(server_addr)

#3.消息发送接收
while True:
    data=input("Msg>>")
    #如果直接回车则跳出循环
    if not data:
        break
    sockfd.send(data.encode())#转换字符串发送
    data=sockfd.recv(1024)
    print("server:",data.decode())

#4.关闭套接字
sockfd.close()