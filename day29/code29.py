""""
基于fork搭建基础网络并发模型
实现步骤
1. 创建监听套接字
2. 等待接收客户端请求
3. 客户端连接创建新的进程处理客户端请求
4. 原进程继续等待其他客户端连接
5. 如果客户端退出,则销毁对应的进程
思路分析:
1.每当有一个客户端酒创建一个新的进程作为客户端处理进程
2.客户端如果结束,对应过程应该销毁
"""
from socket import *
import os
import signal

# 创建监听套接字
HDST = "0.0.0.0"
PORT = 8888
ADDR = (HDST, PORT)


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok")
    c.close()


# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)
# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("Listen the port %d" % PORT)
# 循环等待客户端连接
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理这个客户端
    pid = os.fork()
    if pid == 0:  # 处理客户端请求
        s.close()
        handle(c)  # handle 处理玩客户端请求子进程也退出
        os._exit(0)
    # 无论出错或者父进程都要循环回去接受请求
    # c对于父进程没有用
    c.close()

""""
基于threading的多线程网络并发
实现步骤
1.创建监听套接字
2.循环接收客户端连接请求
3.当有新的客户端连接创建线程处理客户端请求
4.主线程继续等待其他客户端连接
5.当客户端退出,则对应分支线程退出
思路分析：
1.基本与进程相同,只是换为线程处理客户端请求
2.当主线程结束,同时终止所有客户端的请求
"""
from threading import Thread
from socket import *
import sys

# 创建监听套接字
HDST = "0.0.0.0"
PORT = 8888
ADDR = (HDST, PORT)


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok")
    c.close()


# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)
# 循环等待客户端连接
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务端退出")
    except Exception as e:
        print(e)
        continue
    # 创建线程处理客户端请求
    t = Thread(target=handle, args=(c,))
    # daemon为True时主线程退出分支线程也退出
    t.setDaemon(True)
    t.start()
    t.join()

#基于process的进程网络并发


from socket import *
from multiprocessing import Process
import sys
import signal

# 创建监听套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

# 处理客户端请求
def handle(c):
  while True:
    data = c.recv(1024)
    if not data:
      break
    print(data.decode())
    c.send(b'OK')
  c.close()

s = socket()  # tcp套接字
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("Listen the port %d..."%PORT)
# 循环等待客户端连接
while True:
  try:
    c,addr = s.accept()
  except KeyboardInterrupt:
    sys.exit("服务器退出")
  except Exception as e:
    print(e)
    continue

  # 创建进程处理客户端请求
  p = Process(target=handle,args=(c,))
  p.daemon = True
  p.start()
