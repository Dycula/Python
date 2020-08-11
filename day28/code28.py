"""
进程间通信(IPC)
1.必要性:进程间空间独立,资源不共享,此时在需要进程间数据传输时就需要特定的手段进行数据通信。
2.常用进程间通信方法
(1)管道 (2)消息队列 (3)共享内存 (4)信号 (5)信号量 (6)套接字
管道通信(Pipe)
通信原理
在内存中开辟管道空间,生成管道操作对象,多个进程使用同一个管道对象进行读写即可实现通信

实现方法
from multiprocessing import Pipe
fd1,fd2 = Pipe(duplex = True)
功能:创建管道
参数:默认表示双向管道
    如果为False 表示单向管道
返回值:表示管道两端的读写对象
      如果是双向管道均可读写
      如果是单向管道fd1只读 fd2只写

fd.recv()
功能 : 从管道获取内容
返回值:获取到的数据

fd.send(data)
功能: 向管道写入内容
参数: 要写入的数据
"""

from multiprocessing import Pipe, Process
import os, time

# 创建管道对象
fd1, fd2 = Pipe()


def read():
    while True:
        data = fd1.recv()  # 从管道获取消息
        print(data)


def write():
    while True:
        time.sleep(3)
        fd2.send(time.ctime())  # 向管道发送内容


r = Process(target=read)
w = Process(target=write)
r.start()
w.start()
r.join()
w.join()

"""
消息队列
1.通信原理
在内存中建立队列模型,进程通过队列将消息存入,或者从队列取出完成进程间通信。
2. 实现方法
from multiprocessing import Queue
q = Queue(maxsize=0)
功能: 创建队列对象
参数:最多存放消息个数
返回值:队列对象

q.put(data,[block,timeout])
功能:向队列存入消息
参数:data 要存入的内容
block 设置是否阻塞 False为非阻塞
timeout 超时检测

q.get([block,timeout])
功能:从队列取出消息
参数:block 设置是否阻塞 False为非阻塞
timeout 超时检测
返回值: 返回获取到的内容

q.full()    判断队列是否为满    
q.empty()   判断队列是否为空
q.qsize()   获取队列中消息个数
q.close()   关闭队列
"""

from multiprocessing import Process, Queue
from time import sleep
from random import randint

# 创建消息队列
q = Queue(3)


# 请求进程
def request():
    for i in range(10):
        x = randint(0, 100)
        y = randint(0, 100)
        q.put((x, y))


def hardle():
    while True:
        sleep(1)
        try:
            x, y = q.get(timeout=5)
        except:
            break
        else:
            print("%d+%d=%d" % (x, y, x + y))


p1 = Process(target=request)
p2 = Process(target=hardle)
p1.start()
p2.start()
p1.join()
p2.join()

"""
共享内存
1. 通信原理:在内中开辟一块空间,进程可以写入内容和读取内容完成通信,但是每次写入内容会覆盖之前内容。
2. 实现方法
from multiprocessing import Value,Array
obj = Value(ctype,data)
功能 : 开辟共享内存
参数:ctype 表示共享内存空间类型 'i' 'f' 'c'
    data   共享内存空间初始数据
返回值:共享内存对象
obj.value   对该属性的修改查看即对共享内存读写
"""
from multiprocessing import Process, Value
import time
from random import randint

# 创建共享内存
money = Value("i", 5000)


# 修改共享内存
def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += randint(1, 1000)


def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value -= randint(100, 800)


m = Process(target=man)
g = Process(target=girl)
m.start()
g.start()
m.join()
g.join()
# 获取共享内存值
print("一个月余额:", money.value)

"""
obj = Array(ctype,data)
功能: 开辟共享内存空间
参数: ctype 表示共享内存数据类型
      data  整数则表示开辟空间的大小,其他数据类型表示开辟空间存放的初始化数据
返回值:共享内存对象
Array共享内存读写: 通过遍历obj可以得到每个值,直接可以通过索引序号修改任意值。
* 可以使用obj.value直接打印共享内存中的字节串
"""

from multiprocessing import Process, Array

# 创建共享内衬
shm = Array("i", [1, 2, 3])


def fun():
    # 共享内存对象可迭代
    for i in shm:
        print(i)
    shm[1] = 20


p = Process(target=fun)
p.start()
p.join()
for i in shm:
    print(i)

"""
信号量(信号灯集)
通信原理
给定一个数量对多个进程可见。多个进程都可以操作该数量增减,并根据数量值决定自己的行为。

实现方法
from multiprocessing import Semaphore
sem = Semaphore(num)
功能 : 创建信号量对象
参数 : 信号量的初始值
返回值 : 信号量对象

sem.acquire() 将信号量减1 当信号量为0时阻塞
sem.release() 将信号量加1
sem.get_value() 获取信号量数量
"""
from multiprocessing import Process, Semaphore
from time import sleep
import os

# 创建信号量　最多允许三个任务同时执行
sem = Semaphore(3)


# 任务函数
def handle():
    sem.acquire()  # 想执行必须消耗一个信号量
    print("%d执行任务" % os.getpid())
    sleep(2)
    print("%d执行任务完毕" % os.getpid())
    sem.release()  # 增加信号量


# 10个人想执行
for i in range(10):
    p = Process(target=handle)
    p.start()
    p.join()
"""
线程基本概念
1. 什么是线程
【1】 线程被称为轻量级的进程
【2】 线程也可以使用计算机多核资源,是多任务编程方式
【3】 线程是系统分配内核的最小单元
【4】 线程可以理解为进程的分支任务
2. 线程特征
【1】 一个进程中可以包含多个线程
【2】 线程也是一个运行行为,消耗计算机资源
【3】 一个进程中的所有线程共享这个进程的资源
【4】 多个线程之间的运行互不影响各自运行
【5】 线程的创建和销毁消耗资源远小于进程
【6】 各个线程也有自己的ID等特征

threading模块创建线程
【1】 创建线程对象
from threading import Thread
t = Thread()
功能:创建线程对象
参数:target 绑定线程函数
args   元组 给线程函数位置传参
kwargs 字典 给线程函数键值传参
【2】 启动线程    t.start()
【3】 回收线程    t.join([timeout])
"""

import threading
from time import sleep
import os

a = 1


# 线程函数
def music():
    for i in range(3):
        sleep(3)
        print(os.getpid(), "播放黄河大合唱")
    global a
    print("a=", a)
    a = 100


# 创建线程对象
t = threading.Thread(target=music)
t.start()  # 启动线程
for i in range(3):
    sleep(2)
    print(os.getpid(), "播放黄河")
t.join()  # 回收线程
print("Main a:", a)

from threading import Thread
from time import sleep


# 含有参数的线程函数
def fun(sec, name):
    print("线程函数参数")
    sleep(sec)
    print("%s 线程完毕" % name)


# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun, args=(2,), kwargs={"name": "T%d" % i})
    jobs.append(t)
    t.start()
for i in jobs:
    i.join()

"""
线程对象属性
t.name  线程名称
t.setName() 设置线程名称
t.getName() 获取线程名称
t.is_alive() 查看线程是否在生命周期
t.daemon 设置主线程和分支线程的退出关系
t.setDaemon() 设置daemon属性值
t.isDaemon() 查看daemon属性值
daemon为True时主线程退出分支线程也退出。要在start前设置,通常不和join一起使用。
"""

from threading import Thread
from time import sleep


def fun():
    sleep(2)
    print("线程属性测试")


t = Thread(target=fun)

# daemon为True时主线程退出分支线程也退出
t.setDaemon(True)

t.start()

# 设置线程名称
t.setName("Teda")
# 获取线程名称
print("Name:", t.getName())
# 查看线程是否在生命周期
print("Alive:", t.is_alive())

"""
自定义线程类
1. 创建步骤
【1】 继承Thread类
【2】 重写__init__方法添加自己的属性,使用super加载父类属性
【3】 重写run方法
2. 使用方法
【1】 实例化对象
【2】 调用start自动执行run方法
【3】 调用join回收线程
"""

from threading import Thread


class ThreadClass(Thread):
    def __init__(self, attr):
        super().__init__()
        self.attr = attr

    def f1(self):
        print("步骤1")

    def f2(self):
        print("步骤2")

    def run(self):
        self.f1()
        self.f2()


t = ThreadClass("xxx")
t.start()
t.join()
# 练习：
from threading import Thread
from time import sleep, ctime


class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs={}):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args, **self.kwargs)


def player(sec, song):
    for i in range(3):
        print("Playing %s: %s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,), kwargs={"song": "凉凉"})
t.start()
t.join()

"""
同步互斥
线程间通信方法
1. 通信方法
线程间使用全局变量进行通信
2. 共享资源争夺
共享资源:多个进程或者线程都可以操作的资源称为共享资源。对共享资源的操作代码段称为临
界区。
影响 : 对共享资源的无序操作可能会带来数据的混乱,或者操作错误。此时往往需要同步互斥机
制协调操作顺序。
3. 同步互斥机制
同步 : 同步是一种协作关系,为完成操作,多进程或者线程间形成一种协调,按照必要的步骤有
序执行操作。
互斥 : 互斥是一种制约关系,当一个进程或者线程占有资源时会进行加锁处理,此时其他进程线
程就无法操作该资源,直到解锁后才能操作。
线程同步互斥方法

线程Event
from threading import Event
e = Event()     创建线程event对象
e.wait([timeout])   阻塞等待e被set
e.set()   设置e,使wait结束阻塞
e.clear()   使e回到未被设置状态
e.is_set()  查看当前e是否被设置
"""

from threading import Thread, Event
from time import sleep

s = None  # 用于通信
e = Event()  # 创建线程event对象


def yang():
    print("杨子荣拜山头")
    global s
    s = "天王该地虎"
    e.set()  # 对e设置


t = Thread(target=yang)
t.start()
print("说对口令就是自己人")
e.wait()  # 阻塞等待口令说出
if s == "天王该地虎":
    print("宝塔镇河妖")
    print("确认过眼神,是对的人")
else:
    print("打死它")
t.join()

"""
线程锁 Lock
from threading import Lock
lock = Lock() 创建锁对象
lock.acquire() 上锁 如果lock已经上锁再调用会阻塞
lock.release() 解锁
with lock:  上锁
with代码块结束自动解锁
"""
from threading import Thread, Lock

a = b = 0
lock = Lock()  # 定义锁对象


def value():
    while True:
        lock.acquire()  # 上锁
        if a != b:
            print("a=%d,b=%d" % (a, b))
        lock.release()  # 解锁


t = Thread(target=value)
t.start()
while True:
    with lock:
        a += 1
        b += 1
t.join()

import time
import threading


# 交易类
class Account:
    def __init__(self, _id, balance, lock):
        self.id = _id  # 用户
        self.balance = balance  # 存款
        self.lock = lock  # 锁

    # 取钱
    def withdraw(self, amount):
        self.balance -= amount

    # 存钱
    def deposit(self, amount):
        self.balance += amount

    # 查看余额
    def get_balance(self):
        return self.balance


# 创建账户
Tom = Account('Tom', 5000, threading.Lock())
Alex = Account('Alex', 8000, threading.Lock())


# 转账函数
def transfer(from_, to, amount):
    if from_.lock.acquire():  # 锁自己账户
        from_.withdraw(amount)  # 自己账户减少
        time.sleep(0.5)
        if to.lock.acquire():  # 对方账户上锁
            to.deposit(amount)
            to.lock.release()  # 对方账户解锁
        from_.lock.release()  # 自己账户解锁
    print("%s 给 %s转账完成" % (from_.id, to.id))


t1 = threading.Thread(target=transfer,
                      args=(Tom, Alex, 2000))
t2 = threading.Thread(target=transfer,
                      args=(Alex, Tom, 2000))
t1.start()
t2.start()
t1.join()
t2.join()
