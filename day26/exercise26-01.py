# 客户端
from socket import *
import os, sys

# 指定服务端的地址
ADDR = ("176.140.10.215", 2356)


# 发送消息
def send_msg(s, name):
    while True:
        try:
            text = input("发言:")
        except KeyboardInterrupt:
            text = "quit"
        # 退出
        if text == "quit":
            msg = "Q " + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s" % (name, text)
        s.sendto(msg.encode(), ADDR)


# 接收消息
def recv_msg(s):
    while True:
        try:
            data, addr = s.recvfrom(4096)
        except KeyboardInterrupt:
            sys.exit()
        # 服务器发送EXIT退出
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode() + "\n发言：", end=" ")


# 启动客户端
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    while True:
        name = input("请输入姓名:")
        msg = "L " + name
        s.sendto(msg.encode(), ADDR)
        # 等待反馈
        data, addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    # 创建新的进程
    pid = os.fork()
    if pid < 0:
        sys.exit()
    elif pid == 0:
        send_msg(s, name)
    else:
        recv_msg(s)


if __name__ == "__main__":
    main()
