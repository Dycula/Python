"""
ftp 文件服务器
1. 功能
【1】分为服务端和客户端,要求可以有多个客户端同时操作。
【2】客户端可以查看服务器文件库中有什么文件。
【3】客户端可以从文件库中下载文件到本地。
【4】客户端可以上传一个本地文件到文件库。
【5】使用print在客户端打印命令输入提示,引导操作
分析:
1.技术点分析
*并发编程　　多线程并发
*网路传输　　tcp传输
2.结构设计
*客户端发起请求--->界面
list  get filename  put filename
*类封装
3.功能模块
*网络并发结构
*查看文件列表
*下载文件
*上传文件
*退出
4.协议设定
*文件列表查看:只提供普通文件(非隐藏文件)
*客户端请求类型:　 L　文件列表
                G 　filename  下载文件
                p　　filename  上传文件
                Q  　退出
"""
# 服务端
from socket import *
from threading import Thread
import os, time

# 全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)
FTP = "/home/tarena/FTP/"  # 文件库位置


# 创建文件服务器服务端功能
class FTPSever(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    def do_list(self):
        # 获取文件列表
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'ok')
            time.sleep(0.1)
        # 拼接文件列表
        files_ = ""
        for file in files:
            if file[0] != '.' and os.path.isfile(FTP + file):
                files_ += file + "\n"
                self.connfd.send(files_.encode())

    def do_get(self, filename):
        try:
            fd = open(FTP + filename, "rb")
        except Exception:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'ok')
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

    def do_put(self,filename):
        if os.path.exists(FTP+filename):
            self.connfd.send("文件存在".encode())
            return
        self.connfd.send(b"ok")
        f=open(FTP+filename,"wb")
        while True:
            data = f.read(1024)
            if data==b'##':
                break
            f.write(data)
        f.close()

    # 循环接收客户端请求
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == "Q":
                return
            elif data == "L":
                self.do_list()
            elif data[0] == "G":
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == "P":
                filename = data.split(' ')[-1]
                self.do_put(filename)


# 网络搭建
def main():
    # 创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(3)
    print("Listen the port %d" % PORT)
    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            print("服务端程序退出")
        except Exception as  e:
            print(e)
            continue
        # 创建新的线程处理客户端
        client = FTPSever(connfd)
        client.setDaemon(True)
        client.start()  # 运行run方法


if __name__ == "__main__":
    main()
