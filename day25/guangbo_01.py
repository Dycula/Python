#发送广播
from socket import *
import time
#广播地址
dest=("176.140.10.255",1527)
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
data="""
****
6.1儿童节快乐
"""
while True:
    time.sleep(2)
    s.sendto(data.encode(),dest)