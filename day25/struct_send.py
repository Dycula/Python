#客户端
from socket import *
import struct_recv
ADDR=("176.140.10.215",1527)
st=struct_recv.Struct("i32sif")
sockfd=socket(AF_INET,SOCK_DGRAM)
while True:
    print("------")
    id = int(input("学生编号"))
    name = str(input("学生姓名")).encode()
    age = int(input("学生年龄"))
    score = float(input("学生成绩"))

    data=st.pack(id,name,age,score)
    sockfd.sendto(data,ADDR)
sockfd.close()
