"""
电子词典
操作步骤:
(1)确定并发方案,确定套接字的使用,具体细节和需求分析
#frok多进程　　tcp套接字
#注册后进入二级界面,历史记录查询10个
(2)使用dict--->words,还需要什么数据表,数据表设计和创建
#create table dict(id int primary key auto_increment, word varchar(1024) not null,mean varchar(1024) );
#用户表:id name passwd
#create table user(id int primary key auto_increment,name varchar(32) not null,passwd varchar(128) not null,);
#历史记录:id name word time
#create table hist(id int primary key auto_increment,naem varchar(32) not null, word varchar(32) not null,time datetime default now());
(3)结构设计,如何封装,客户端服务端工作流程
#客户端(发请求,展示结果)
#服务端(逻辑操作,解决请求)
#数据操作端(操作数据库)
界面处理
    while True:
        界面1
        while True:
            界面2
(4)功能模块划分
#网络搭建
服务端功能:业务逻辑功能
模型:多进程　tcp　并发
客户端功能:根据用户输入,发送请求得到结果
结构:一级界面--->注册　登录退出
二级界面--->查单词　历史记录　注销
#注册:客户端 R name passwd
#登录:客户端　L name passwd
#查单词
#历史记录
"""
from socket import *
from multiprocessing import Process
import signal, sys
from day35.project_02 import *
from time import sleep

# 全局变量
HOST = "0.0.0.0"
PORT = 8765
ADDR = (HOST, PORT)

# 数据库对象
db = Database()


# 注册处理
def do_register(c, data):
    tmp = data.split(" ")
    name = tmp[1]
    passwd = tmp[2]
    if db.register(name, passwd):
        c.send(b"ok")
    else:
        c.send(b"Fail")


# 登录处理
def do_login(c, data):
    tmp = data.split(" ")
    name = tmp[1]
    passwd = tmp[2]
    if db.login(name, passwd):
        c.send(b"ok")
    else:
        c.send(b"Fail")


# 查询单词
def do_query(c, data):
    tmp = data.split(" ")
    name = tmp[1]
    word = tmp[2]
    #插入历史记录
    db.insert_history(name,word)
    #找到返回解释,没有找到返回None
    mean=db.query(word)
    if not mean:
        c.send("没有找到单词".encode())
    else:
        msg = "%s : %s" % (word, mean)
        c.send(msg.encode())
#历史记录
def do_hist(c,data):
    name=data.split(" ")[1]
    r=db.history(name)
    if not r:
        c.send(b"Fail")
        return
    c.send(b"ok")
    for i in r:
        #i-->(name,word,time)
        msg="%s %-16s %s"%i
        sleep(0.1)
        c.send(msg.encode())
    sleep(0.1)
    c.send(b"##")


# 接收客户端请求,分析处理函数
def request(c):
    db.create_cursor()  # 生成游标
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(), ":", data)
        if not data or data[0] == "E":
            sys.exit("感谢使用")
        if data[0] == "R":
            do_register(c, data)
        elif data[0] == "L":
            do_login(c, data)
        elif data[0] == "Q":
            do_query(c, data)
        elif data[0] == "H":
            do_hist(c, data)


# 搭建网络
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)
    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    # 循环等待客户端连接
    print("Listen the port....")
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            db.close()
            sys.exit("服务端退出")
        except Exception as e:
            print(e)
            continue
        # 为客户端创建子进程
        p = Process(target=request, args=(c,))
        p.daemon = True
        p.start()


if __name__ == "__main__":
    main()
