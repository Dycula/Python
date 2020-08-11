"""
多任务编程
1. 意义:充分利用计算机多核资源,提高程序的运行效率.
2. 实现方案 :多进程,多线程
3. 并行与并发
并发:同时处理多个任务,内核在任务间不断的切换达到好像多个任务被同时执行的效果,实际
每个时刻只有一个任务占有内核.
并行:多个任务利用计算机多核资源在同时执行,此时多个任务间为并行关系。
"""
"""
进程理论基础
1. 定义:程序在计算机中的一次运行。
程序是一个可执行的文件,是静态的占有磁盘。
进程是一个动态的过程描述,占有计算机运行资源,有一定的生命周期。
2. 系统中如何产生一个进程
【1】用户空间通过调用程序接口或者命令发起请求
【2】操作系统接收用户请求,开始创建进程
【3】操作系统调配计算机资源,确定进程状态等
【4】操作系统将创建的进程提供给用户使用
3. 进程基本概念
cpu时间片:如果一个进程占有cpu内核则称这个进程在cpu时间片上。
PCB(进程控制块):在内存中开辟的一块空间,用于存放进程的基本信息,也用于系统查找识别进
程。
进程ID(PID):系统为每个进程分配的一个大于0的整数,作为进程ID。每个进程ID不重复。
Linux查看进程ID : ps -aux
父子进程:系统中每一个进程(除了系统初始化进程)都有唯一的父进程,可以有0个或多个子进
程。父子进程关系便于进程管理。
查看进程树:pstree
进程状态
三态
就绪态:进程具备执行条件,等待分配cpu资源
运行态:进程占有cpu时间片正在运行
等待态:进程暂时停止运行,让出cpu
五态 (在三态基础上增加新建和终止)
新建 : 创建一个进程,获取资源的过程
终止 : 进程结束,释放资源的过程
进程的运行特征
【1】 进程可以使用计算机多核资源
【2】 进程是计算机分配资源的最小单位
【3】 进程之间的运行互不影响,各自独立
【4】 每个进程拥有独立的空间,各自使用自己空间资源
"""

#基于fork的进程创建
import os
pid=os.fork()
#print(pid)
if pid<0:
    print("Create process failed")
elif pid==0:
    print("New process")
else:
    print("Old process")
print("Fork test end")

import os
from time import sleep
print("=========================")
a = 1
pid = os.fork()
if pid < 0:
  print("Create process failed")
elif pid == 0:
  print("New process")
  print("a = ",a)
  a = 10000
else:
  sleep(1)
  print("Old process")
  print("a:",a)
print("All a = ",a)
#获取pid值
# os.getpid()
# 功能: 获取一个进程的PID值
# 返回值: 返回当前进程的PID

# os.getppid()
# 功能: 获取父进程的PID号
# 返回值: 返回父进程PID
import os
pid=os.fork()
if pid<0:
    print("Error")
elif pid==0:
    print("Child PID:",os.getpid())
    print("Get parent PID:",os.getppid())
else:
    print("Get child PID:",pid)
    print("parent PID:",os.getpid())

#os._exit(status)
# 功能: 结束一个进程
# 参数:进程的终止状态
# sys.exit([status])
# 功能:退出进程
# 参数:整数 表示退出状态
# 字符串 表示退出时打印内容
import os
import sys
os._exit(1)
print("Process exit")

#如何避免僵尸进程产生
# (1)使用wait函数处理子进程退出
import os
pid=os.fork()
if pid<0:
    print("Error")
elif pid==0:
    print("Child process",os.getpid())
    os._exit(5)
else:
    p,status=os.wait()#阻碍等待子进程退出
    print("p:",p)
    print("status:",os.WEXITSTATUS(status))
    while True:
        pass
        
#(2)创建二级子进程处理僵尸
import os
from time import sleep
def f1():
    for i in range(4):
        sleep(2)
        print("写代码")

def f2():
    for i in range(5):
        sleep(1)
        print("测代码")
pid =os.fork()
if pid<0:
    print("Error")
elif pid==0:
    pid01=os.fork()#二级子进程
    if pid01==0:
        f2()
    else:
        os._exit(0)#一级子进程退出
else:
    os.wait()#等一级子进程退出
    f1()

#(3)通过信号处理子进程退出
import  signal
import os
#子进程退出时父进程会忽略，此时子进程自动由系统处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
pid=os.fork()
#print(pid)
if pid<0:
    pass
elif pid==0:
    print("Child process",os.getpid())
else:
    while True:
        pass
#练习:创建父子进程,复制一个文件,各自复制一半到新的文件中

import os
filename = "./img.jpg"
size = os.path.getsize(filename)
# 父子进程使用fr会相互影响
# fr = open(filename, 'rb')
def top():
  fr = open(filename,'rb')
  fw = open('top.jpg','wb')
  n = size // 2
  fw.write(fr.read(n))
  fr.close()
  fw.close()
def bot():
  fr = open(filename, 'rb')
  fw = open('bot.jpg', 'wb')
  fr.seek(size//2,0)
  fw.write(fr.read())
  fr.close()
  fw.close()
pid = os.fork()
if pid < 0:
  print("Error")
elif pid == 0:
  top()  # 复制上半部分
else:
  bot()  # 下半部分
#总结:父进程中生成文件描述符,子进程从父进程拷贝,此时父子进程对该文件描述符的使用相互会有影响
#如果父子进程中各自生成的文件描述符,那么相互之间没有任何影响


