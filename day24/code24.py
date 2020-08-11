"""
套接字
1.流式套接字(SOCK_STREAM): 以字节流方式传输数据,实现tcp网络传输方案。
(面向连接--tcp协议--可靠的--流式套接字)
2.数据报套接字(SOCK_DGRAM):以数据报形式传输数据,实现udp网络传输方案。
(无连接--udp协议--不可靠--数据报套接字)
"""
"""
tcp套接字服务端流程
"""
import socket

#1.创建流式套接字
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM,proto=0)

#2.绑定地址
sockfd.bind(("176.140.10.215",8888))

#3.设置sockfd为监听套接字
sockfd.listen(3)

#4.等待处理客户端链接请求
while True:
    print("Waiting for connect....")
    try:
        connfd,addr=sockfd.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        print("server exit")
        break

    #5.接收消息
    while True:
        data=connfd.recv(1024)
        if not data:
            break
        print("Message:",data.decode())
        n=connfd.send(b"*hello*")
        print("Send %d bytes"%n)

    #6.关闭套接字
    connfd.close()  #断开链接
sockfd.close()

