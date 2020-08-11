"""
网络收发缓冲区
1.网络缓冲区有效的协调了消息的收发速度
2.send和recv实际是向缓冲区发送接收消息,当缓冲区不为空recv就不会阻塞

cp粘包
原因:tcp以字节流方式传输,没有消息边界.多次发送的消息被一次接收,此时就会形成粘包.
影响:如果每次发送内容是一个独立的含义,需要接收端独立解析此时粘包会有影响.
处理方法
    1. 人为的添加消息边界
    2. 控制发送速度
"""
"""
tcp 粘包
"""

from socket import *

sockfd = socket()

server_addr = ("127.0.0.1",8888)
sockfd.connect(server_addr)

while True:
  sockfd.send(b'hello')

sockfd.close()



#udp套接字服务端流程
from socket import *
#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
#绑定地址
server_addr=("176.140.10.215",8888)
sockfd.bind(server_addr)
#接收信息
while True:
    data,addr=sockfd.recvfrom(1024)
    print("收到的消息：",data.decode())
    sockfd.sendto(b'Receive',addr)
#关闭套接字
sockfd.close()
"""
总结 :tcp套接字和udp套接字编程区别
1. 流式套接字是以字节流方式传输数据,数据报套接字以数据报形式传输
2. tcp套接字会有粘包,udp套接字有消息边界不会粘包
3. tcp套接字保证消息的完整性,udp套接字则不能
4. tcp套接字依赖listen accept建立连接才能收发消息,udp套接字则不需要
5. tcp套接字使用send,recv收发消息,udp套接字使用sendto,recvfrom
"""
#练习:使用udp完成单词查询,要求一个服务端拥有单词本,从客户端可以循坏输入单词,得到单词解释,客户端可以直接回车或者发送特殊字符表示退出
from socket import *
DICT_TEXT = './dict.txt'
def find_word(word):
    file = open(DICT_TEXT)
    for line in file:
        total_word = line.split(" ")[0]
        if total_word > word:
            return "没有找到该单词"  # 遍历的单词大于目标
        elif total_word == word:
            return line
        else:
           return "没有找到该单词"
sockfd=socket(AF_INET,SOCK_DGRAM)
server_addr=("176.140.10.215",8888)
while True:
    data,addr=sockfd.recvfrom(1024)
    mean=find_word(data.decode())
    sockfd.sendto(mean.encode(), addr)
sockfd.close()

"""
套接字属性
"""
from socket import *
#创建套接字
s=socket()
#设置套接字端口立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("176.140.10.215",8888))
s.listen(3)
c,addr=s.accept()
#套接字地址类型
print("地址类型:",s.family)
#套接字类型
print("套接字类型：",s.type)
#获取套接字绑定地址
print("绑定的地址:",s.getsockname())
#获取套接字的文件描述符
print("获取文件描述符:",s.fileno())
#获取连接套接字客户端地址
print("获取连接的客户端地址:",c.getpeername())
#获取选项值
print("获取选项值:",s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

#请求响应
from socket import *
s=socket()
s.bind(("0.0.0.0",0000))
s.listen(3)
c,adr=s.accept()
print("Connect from",addr)
data=c.recv(1024)

print(data)
c.close()
s.close()



#复习:
# tcp套接字中的缓冲区和粘包
# udp套接字编程
# tcp和udp编程差异
# 广播
# http协议
# http协议是干什么的有什么基本特点
# http请求和响应的格式,每部分的作用
# http请求类型及含义和响应码类型及含义

