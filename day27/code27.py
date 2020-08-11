"""
multiprocessing 模块创建进程
 流程特点
【1】将需要子进程执行的事件封装为函数
【2】通过模块的Process类创建进程对象,关联函数
【3】可以通过进程对象设置进程信息及属性
【4】通过进程对象调用start启动进程
【5】通过进程对象调用join回收进程
Process()
功能 : 创建进程对象
参数 : target 绑定要执行的目标函数
args 元组,用于给target函数位置传参
kwargs 字典,给target函数键值传参
p.start()
功能 : 启动进程
p.join([timeout])
功能:阻塞等待回收进程
参数:超时时间
"""
import multiprocessing as mp
from time import sleep
a=1
def fun():
    print("开始一个新的进程")
    sleep(3)
    global a
    print("a=",a)
    print("子进程结束")
#创建进程对象
p=mp.Process(target=fun)
p.start()#启动进程
sleep(2)
print("父进程")
p.join(1)#回收进程
print("a=",a)
#等价于如下
# import os
# pid=os.fork()
# if pid==0:
#     fun()
# else:
#     os.wait()


from multiprocessing import Process
from time import sleep
import os


def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(), "----", os.getpid())


def th2():
    sleep(3)
    print("睡觉")
    print(os.getppid(), "----", os.getpid())


def th3():
    sleep(3)
    print("打豆豆")
    print(os.getppid(), "----", os.getpid())


things = [th1, th2, th3]
jobs = []
for th in things:
    p = Process(target=th)
    p.start()
    jobs.append(p)  # 将进程对象保存在列表
#一起回收
for i in jobs:
    i.join()


from multiprocessing import Process
from time import sleep
#带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I am %s"%name)
        print("I am working")
#p=Process(target=worker,args=(2,"Baron"))
p=Process(target=worker,kwargs={"sec":2,"name":"Baron"})
p.start()
p.join()

"""""
进程对象属性
p.name 进程名称
p.pid 对应子进程的PID号
p.is_alive() 查看子进程是否在生命周期
p.daemon 设置父子进程的退出关系
"""""
from multiprocessing import Process
from time import sleep, ctime


def tm():
    for i in range(3):
        sleep(2)
        print(ctime())


p = Process(target=tm)
p.daemon = True  # 子进程会随父进程退出
p.start()
p.join()
print("Name:", p.name)  # 名称
print("PID:", p.pid)  # PID
print("Is alive:", p.is_alive())  # 生命周期

"""""
进程池实现
【1】 创建进程池对象,放入适当的进程
from multiprocessing import Pool
Pool(processes)
功能: 创建进程池对象
参数: 指定进程数量,默认根据系统自动判定
【2】 将事件加入进程池队列执行
pool.apply_async(func,args,kwds)
功能: 使用进程池执行 func事件
参数: func 事件函数
args 元组 给func按位置传参
kwds 字典 给func按照键值传参
返回值: 返回函数事件对象
【3】 关闭进程池
pool.close()
功能: 关闭进程池
【4】 回收进程池中进程
pool.join()
功能: 回收进程池中进程
"""
from multiprocessing import Pool
from time import sleep, ctime


# 进程池事件
def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

# 创建进程池
pool = Pool()
# 向进程池添加执行事件
for i in range(20):
    msg = "hello %d" % i
    r=pool.apply_async(func=worker, args=(msg,))
# 关闭进程池
pool.close()
# 回收进程池
pool.join()
print(r.get())#可以获取事件函数的返回值
