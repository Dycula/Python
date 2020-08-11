"""
HTTPServer v2.0
1.主要功能 :
【1】接收客户端(浏览器)请求
【2】解析客户端发送的请求
【3】根据请求组织数据内容
【4】将数据内容形参http响应格式返回给浏览器
2.升级点 :
【1】采用IO并发,可以满足多个客户端同时发起请求情况
【2】做基本的请求解析,根据具体请求返回具体内容,同时满足客户端简单的非网页请求情况
【3】通过类接口形式进行功能封装
接口设计:
*提供句柄,通过句柄调用属性方法解决问题
fd=open()
sockfd=socket()
lock=lock()
db=putmysql.connect()
*实例化对象,通过对象设置,启动服务
t=Thread()
p=Process()
s=socketserver()
*根据功能需求,如果无法替用户决定的内容,通过参数传递
*能够解决的问题,不要让用户解决,需要用户解决的问题可以用重写的方式让用户重写
技术分析:
1.HTTP协议熟悉
2.select并发
3.tcp套接字
思路分析:
1.使用类进行封装
2.从用户使用角度决定类的编写
"""
from socket import *
from select import select


# 具体httpserver功能
class HTTPServer:
    def __init__(self, host, port, dir):
        # 添加属性
        self.address = (host, port)
        self.host = host
        self.port = port
        self.dir = dir
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self):
        self.sockfd.bind(self.address)

    # 启动服务
    def server_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d" % self.port)
        self.rlist.append(self.sockfd)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print("Connect from ", addr)
                    self.rlist.append(c)
                else:
                    # 处理请求
                    self.handle(r)

    # 具体处理请求
    def handle(self, connfd):
        # 接收http请求
        request = connfd.recv(4096)
        # 防止客户端断开
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        # 提取请求内容
        request_line = request.splitlines()[0]
        info = request_line.decode().split(' ')[1]
        print(connfd.getpeername(), ":", info)
        if info == "/" or info[-5:] == '.html':
            self.get_html(connfd, info)

    # 处理网页请求
    def get_html(self, connfd, info):
        if info == "/":
            filename = self.dir + "/index.html"
        else:
            filename = self.dir + info
        try:
            fd = open(filename)
        except Exception:
            # 没有网页
            responseHeaders = "HTTP/1.1 404 Found\r\n"
            responseHeaders += "\r\n"
            responseBody = "<h1>  Sorry..</h1>"
        else:
            # 存在网页
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            responseBody = fd.read()
        finally:
            response = responseHeaders + responseBody
            # 发送给浏览器
            connfd.send(response.encode())


if __name__ == "__main__":
    # 希望通过HTTPServer类快速搭建http服务来展示自己的网页
    # 用户自己决定的内容
    HOST = "127.0.0.1"
    PORT = 8765
    DIR = "./static"  # 网页存储位置
    httpd = HTTPServer(HOST, PORT, DIR)  # 实例化对象
    httpd.server_forever()  # 启动http服务　

"""
协程技术
基础概念
1.定义:纤程,微线程。是为非抢占式多任务产生子程序的计算机组件。协程允许不同入口点在不
同位置暂停或开始,简单来说,协程就是可以暂停执行的函数。
2.协程原理:记录一个函数的上下文栈帧,协程调度切换时会将记录的上下文保存,在切换回来时
进行调取,恢复原有的执行内容,以便从上一次执行位置继续执行。
3.协程优缺点
优点
1.协程完成多任务占用计算资源很少
2.由于协程的多任务切换在应用层完成,因此切换开销少
3.协程为单线程程序,无需进行共享资源同步互斥处理
缺点:协程的本质是一个单线程,无法利用计算机多核资源

第三方协程模
1. greenlet模块
greenlet.greenlet(func)
功能:创建协程对象
参数:协程函数
g.switch()
功能:选择要执行的协程函数
"""
from greenlet import greenlet


def test1():
    print("执行test1")
    print("结束test1")


def test2():
    print("执行test2")
    print("结束test2")


# 将函数变成协程
gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()  # 选择执行协程1

"""
gevent模块
gevent.spawn(func,argv)
功能: 生成协程对象
参数:func 协程函数
     argv 给协程函数传参(不定参)
返回值: 协程对象

gevent.joinall(list,[timeout])
功能: 阻塞等待协程执行完毕
参数:list 协程对象列表
     timeout 超时时间
     
gevent.sleep(sec)
功能: gevent睡眠阻塞
参数:睡眠时间
gevent协程只有在遇到gevent指定的阻塞行为时才会自动在协程之间进行跳转
如gevent.joinall(),gevent.sleep()带来的阻塞
"""
import gevent
from time import sleep


def fun(a, b):
    print("Running fun ", a, b)
    gevent.sleep(3)
    print("fun again")


def fun1():
    print("Running fun1 ")
    gevent.sleep(5)
    print("fun1 again")


f = gevent.spawn(fun, 1, 2)
a = gevent.spawn(fun1)
gevent.joinall([f, a])  # 阻塞等待列表中的协程结束
"""
monkey脚本
作用:在gevent协程中,协程只有遇到gevent指定类型的阻塞才能跳转到其他协程,因此,我们
希望将普通的IO阻塞行为转换为可以触发gevent协程跳转的阻塞,以提高执行效率。
转换方法:gevent 提供了一个脚本程序monkey,可以修改底层解释IO阻塞的行为,将很多普通阻
塞转换为gevent阻塞。
使用方法
【1】 导入monkey
from gevent import monkey
【2】 运行相应的脚本,例如转换socket中所有阻塞
monkey.patch_socket()
【3】 如果将所有可转换的IO阻塞全部转换则运行all
monkey.patch_all()
【4】 注意:脚本运行函数需要在对应模块导入前执行
"""
import gevent
from gevent import monkey

monkey.patch_all()  # 在导入socket前执行
from socket import *


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()


# 创建tcp套接字
s = socket()
s.bind(("0.0.0.0", 8888))
s.listen(3)
while True:
    c, addr = s.accept()
    print("Connect from ", addr)
    #handle(c)
    gevent.spawn(handle(c))
s.close()

# 函数式编程
# 面向对象的程序设计
# 装饰器
# 网络编程
# 进程线程io模型
# 基础算法