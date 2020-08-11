"""
非阻塞IO
1.定义 :通过修改IO属性行为,使原本阻塞的IO变为非阻塞的状态

设置套接字为非阻塞IO
sockfd.setblocking(bool)
功能:设置套接字为非阻塞IO
参数:默认为True,表示套接字IO阻塞;设置为False则套接字IO变为非阻塞

超时检测 :设置一个最长阻塞时间,超过该时间后则不再阻塞等待。
sockfd.settimeout(sec)
功能:设置套接字的超时时间
参数:设置的时间
"""

from socket import *
from time import sleep, ctime

# 日志文件
f = open("log.txt", "a+")
# 创建套接字
sockfd = socket()
sockfd.bind(("127.0.0.1", 8756))
sockfd.listen(3)
#设置套接字为非阻塞
#sockfd.setblocking(False)
#设置超时检测
sockfd.settimeout(3)
while True:
    print("Waiting for connect ....")
    try:
        connfd, addr = sockfd.accept()
    except (BlockingIOError,timeout) as e:
        # 如果没有客户端连接,每隔3秒填充一个日志
        f.write("%s: %s\n"%(ctime(),e))
        f.flush()
        sleep(3)
    else:
        print("Connect from",addr)
        data=connfd.recv(1024).decode()
        print(data)


"""
select 方法
rs, ws, xs=select(rlist, wlist, xlist[, timeout])
功能: 监控IO事件,阻塞等待IO发生
参数:rlist 列表 存放关注的等待发生的IO事件
     wlist 列表 存放关注的要主动处理的IO事件
     xlist 列表 存放关注的出现异常要处理的IO
     timeout 超时时间
返回值: rs 列表 rlist中准备就绪的IO
       ws 列表 wlist中准备就绪的IO
       xs 列表 xlist中准备就绪的IO
       
select 实现tcp服务
【1】将关注的IO放入对应的监控类别列表
【2】通过select函数进行监控
【3】遍历select返回值列表,确定就绪IO事件
【4】处理发生的IO事件
"""
from socket import *
from select import select

# 创建一个监听套接字作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8765))
s.listen(3)
# 设置关注列表
rlist = [s]
wlist = []
xlist = []
# 循环监控IO
while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    # 遍历三个返回列表,处理IO
    for r in rs:
        # 根据遍历到了IO 的不同使用if分情况处理
        if r is s:
            c, addr = r.accept()
            print("Connect from", addr)
            rlist.append(c)  # 增加新的IO事件
        # else为客户端套接字就绪情况
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue  # 继续处理其他就绪IO
            print("Receive:", data.decode())
            # r.send(b'ok')
            # 我们希望主动处理这个IO对象
            wlist.append(r)
    for w in ws:
        w.send(b'ok')
        wlist.remove(w)
    for x in xs:
        pass

"""
poll方法
p = select.poll()
功能 : 创建poll对象
返回值: poll对象

p.register(fd,event)
功能: 注册关注的IO事件
参数:fd 要关注的IO
    event 要关注的IO事件类型
常用类型:
POLLIN  读IO事件(rlist)
POLLOUT 写IO事件 (wlist)
POLLERR 异常IO (xlist)
POLLHUP 断开连接
e.g. p.register(sockfd,POLLIN|POLLERR)

p.unregister(fd)
功能:取消对IO的关注
参数:IO对象或者IO对象的fileno

events = p.poll()
功能: 阻塞等待监控的IO事件发生
返回值: 返回发生的IO
events格式 [(fileno,event),()....]
每个元组为一个就绪IO,元组第一项是该IO的fileno,第二项为该IO就绪的事件类型

poll_server 步骤
【1】创建套接字为监控IO
【2】将套接字register
【3】创建查找字典,并维护(要时刻注册IO保持一致)
【4】循环监控IO发生
【5】处理发生的IO
"""
from socket import *
from select import *

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8765))
s.listen(3)
# 创建poll对象关注s
p = poll()
# 建立查找字典,用于通过fileno查找IO对象
fdmap = {s.fileno(): s}
# 关注s
p.register(s, POLLIN | POLLERR)
# 循环监控IO
while True:
    events = p.poll()
    # 循环遍历发生的事件fd--->fileno
    for fd, event in events:
        # 区分事件进行处理
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect from", addr)
            # 添加新的关注IO
            p.register(c, POLLIN)
            fdmap[c.fileno()] = c  # 维护字典
        # 按位与判定POLLIN就绪
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)  # 取消关注
                famap[fd].close()
                del fdmap[fd]  # 从字典中删除
                continue
            print("Receive:", data.decode())
            fdmap[fd].send(b'ok')
"""
epoll方法
1. 使用方法 : 基本与poll相同
生成对象改为 epoll()
将所有事件类型改为EPOLL类型
2. epoll特点
epoll 效率比select poll要高
epoll 监控IO数量比select要多
epoll 的触发方式比poll要多 (EPOLLET边缘触发)
"""
from socket import *
from select import *

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8765))
s.listen(3)
# 创建poll对象关注s
p = epoll()
# 建立查找字典,用于通过fileno查找IO对象
fdmap = {s.fileno(): s}
# 关注s
p.register(s, EPOLLIN | EPOLLERR)
# 循环监控IO
while True:
    events = p.epoll()
    # 循环遍历发生的事件fd--->fileno
    for fd, event in events:
        # 区分事件进行处理
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect from", addr)
            # 添加新的关注IO
            p.register(c, EPOLLIN)
            fdmap[c.fileno()] = c  # 维护字典
        # 按位与判定POLLIN就绪
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)  # 取消关注
                famap[fd].close()
                del fdmap[fd]  # 从字典中删除
                continue
            print("Receive:", data.decode())
            fdmap[fd].send(b'ok')