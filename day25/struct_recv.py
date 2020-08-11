"""
struct模块的使用
1. 原理: 将一组简单数据进行打包,转换为bytes格式发送.或者将一组bytes格式数据,进行解
析.
2. 接口使用
"""
# 练习:使用udp完成
# 从客户端循环输入学生信息,包含编号(整型),姓名(字符串),年龄(整型),
# 分数(浮点型,精确到小数点后一位),将其发送到服务端
# 服务端将收到的内容写入到一个文件里,每个学生信息占一行
#服务端
from socket import *
import struct_recv
#udp套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
sockfd.bind(("176.140.10.215",1527))
#数据结构
st=struct_recv.Struct("i32sif")
#打开文件
f=open("student,txt","a")

while True:
    data,addr = sockfd.recvfrom(1024)
    data=st.unpack(data)#解析数据
    info="%d %-10s %d %.1f\n"%(data[0],data[1].encode(),data[2],data[3])
    f.write()
    f.flush()
sockfd.close()
