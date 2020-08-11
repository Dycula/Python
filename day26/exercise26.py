"""
练习:网络聊天室
功能 : 类似qq群功能
【1】 有人进入聊天室需要输入姓名,姓名不能重复
【2】 有人进入聊天室时,其他人会收到通知:xxx 进入了聊天室
【3】 一个人发消息,其他人会收到:xxx : xxxxxxxxxxx
【4】 有人退出聊天室,则其他人也会收到通知:xxx退出了聊天室
【5】 扩展功能:服务器可以向所有用户发送公告:管理员消息: xxxxxxxxx
思路分析:
1.功能和需求的分析
2.技术分析
客户端
服务端
网络:udp
用户信息存储(name:address)
           [(name,address),()]
           链表　　data--->(name,address)
客户端的收发消息:多进程分别处理收发
3.结构设计
采用函数封装
注意:(1)注释的添加(2)功能测试
4.分析功能模块,指定编写流程
(1)搭建网络连接
(2)进入聊天室
客户端:(1)输入姓名(2)将姓名发送给服务端(3)收到服务器反馈(4)进入聊天室或者重新输入姓名
服务端:(1)收到请求(2)判断姓名是否存在(3)反馈信息给客户端(4)不允许进入结束,允许进入将用户插入字典(5)通知其他用户
允许进入则服务端给客户端发送：ok
不允许进入则服务端给客户端发送:不允许进入的原因
(3)聊天
客户端:(1)创建新的进程(2)父进程接收消息(3)子进程发送消息
服务端:(1)接收请求(2)将消息发送给其他人
(4)退出聊天室
客户端:(1)输入退出(2)将请求发送给服务端(3)结束进程发送进程(4)接收EXIT退出
服务端:(1)接收请求(2)将退出消息发送给其他人(3)给退出的客户端发送 "EXIT"(4)删除用户
(5)管理员消息
5.存储用户结构:(name:address)
请求类型:进入聊天室L name
聊天信息:C name content
退出聊天:Q name
"""
# 服务端
from socket import *
import os, sys

# 服务器地址
ADDR = ("176.140.10.215", 2356)
# 存储用户(name:address)
user = {}


# 登录
def do_login(s, name, addr):
    if name in user or "管理员" in name:
        s.sendto("该用户已经存在".encode(), addr)
        return
    s.sendto(b'OK', addr)
    # 通知其他人
    msg = "\n发送%s进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    # 插入字典
    user[name] = addr


def do_chat(s, name, text):
    msg = "\n%s : %s" % (name, text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])


def do_quit(s, name):
    msg = "\n%s退出聊天室" % name
    for i in name:
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.send(b'EXIT', user[i])
    # 从字典中移除
    del user[name]


# 循环接收客户端的请求
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        tmp = data.decode().split(' ')  # 拆分请求
        # 根据请求类型执行不同内容
        if tmp[0] == "L":
            do_login(s, tmp[1], addr)  # 完成具体服务端登录工作
        elif tmp[0] == "C":
            text = ' '.join(tmp[2:])  # 拼接消息内容
            do_chat(s, tmp[1], text)
        elif tmp[0] == "Q":
            if tmp[1] not in user:
                s.sendto(b'EXIT', addr)
                continue
            do_quit(s, tmp[1])


# 搭建udp网络
def main():
    # udp套接字
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid < 0:
        return
    elif pid == 0:
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员消息 " + msg
            s.sendto(msg.encode(), ADDR)
    else:
        # 请求处理函数
        do_request(s)


if __name__ == "__main__":
    main()

"""
1.struct 模块
2.什么是多任务编程
3.并发与并行
4.动态　　有周期　占有运行周期
5.进程概念:pid 父子进程　pcb  进程状态
6.fork的使用
7.进程函数:
    os.getpid()
    os.getppid()
    os._exit()
    sys.exit()
8.孤儿与僵尸:wait函数　二级子进程　sinagal
9.文件描述符的使用
"""
