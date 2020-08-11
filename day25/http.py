""""
网页请求过程
1.客户端(浏览器)通过tcp传输,发送http请求给服务端
2.服务端接收到http请求后进行解析
3.服务端处理请求内容,组织响应内容
4.服务端将响应内容以http响应格式发送给浏览器
5.浏览器接收到响应内容,解析展示
"""
# 发送网页给浏览器
from socket import *

# 处理客户端请求
def handle(connfd):
    request = connfd.recv(4096)
    if not request:
        return
    request_line = request.splitlines()[0]
    info = request_line.decode().split(" ")[1]
    if info == "/":
        with open("index.html") as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()
    else:
        response = "HTTP/1.1 404 Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry..</h1>"
    # 发送给浏览器
    connfd.send(response.encode())


# 搭建一个tcp网络
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sockfd.bind(("176.140.10.215", 3698))
sockfd.listen(3)
while True:
    connfd, addr = sockfd.accept()
    handle(connfd)  # 处理客户端请求
