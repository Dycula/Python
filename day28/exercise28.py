"""
前情回顾

1.聊天室
需求分析 --> 技术分析 --> 结构设计 --> 功能模块设计 --> 协议设计

2.multiprocessing创建进程
Process()创建进程对象
start()启动进程
join()回收进程

3.进程对象属性
p.pid
p.name
p.is_alive()
p.daemon
4.进程池
Pool()
apply_async()
close()
join()

** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *

进程:
1.理论
2.fork
3.Process
4.进程池
5.进程间通信

进程通信方法
1.管道通信：pipe()   recv()   send()
消息队列: Queue()    put()   get()
共享内存: Value()    Array()
信号量:  Semaphore()
线程创建　threading
Thread()  创建线程对象
start()   启动线程
join()    回收线程
线程对象属性: name   daemon
自定义线程类
*继承Thread
*重写__init__   run
同步互斥方法
Event:  e.set()  e.clear()  e.wait()
Lock:lock.acquire()   lock.release()
死锁:导致程序阻塞,无法运行

作业:
1.做进程 线程 单进程的效率测试
使用单进程分别执行count io 10遍记录时间使用10个线程,
每个线程执行count io 1次记录时间使用10个进程,
每个进程执行count io 1次记录时间
2.总结进程线程的差别
"""

