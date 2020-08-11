"""
http server 2.0
io多路复用　ｈｔｔｐ　练习

思路分析：
1.　使用类进行封装
2.　从用户使用角度决定类的编写
"""
from socket import *
from select import select


# 　具体ＨＴＴＰ　ｓｅｖｅｒ功能
class HTTPServer:
  def __init__(self, host, port, dir):
    # 　添加属性
    self.address = (host, port)
    self.host = host
    self.port = port
    self.dir = dir
    self.rlist = []
    self.wlist = []
    self.xlist = []
    self.create_socket()
    self.bind()

  # 创建套接字
  def create_socket(self):
    self.sockfd = socket()
    self.sockfd.setsockopt(SOL_SOCKET,
                           SO_REUSEADDR, 1)

  def bind(self):
    self.sockfd.bind(self.address)

  # 　启动服务
  def serve_forever(self):
    self.sockfd.listen(5)
    print("Listen the port %d" % self.port)
    self.rlist.append(self.sockfd)
    while True:
      rs, ws, xs = select(self.rlist, self.wlist,
                          self.xlist)
      for r in rs:
        if r is self.sockfd:
          c, addr = r.accept()
          print("Connect from", addr)
          self.rlist.append(c)
        else:
          # 　处理请求
          self.handle(r)

  # 具体处理请求
  def handle(self, connfd):
    # 　接收http请求
    request = connfd.recv(4096)
    # 　防止客户端断开
    if not request:
      self.rlist.remove(connfd)
      connfd.close()
      return

    # 提取请求内容
    request_line = request.splitlines()[0]
    info = request_line.decode().split(' ')[1]
    print(connfd.getpeername(), ":", info)

    # 　ｉｎｆｏ分为访问网页或者其他内容
    if info == '/' or info[-5:] == '.html':
      self.get_html(connfd, info)
    else:
      pass

  # 处理网页请求
  def get_html(self, connfd, info):
    if info == '/':
      filename = self.dir + "/index.html"
    else:
      filename = self.dir + info
    try:
      fd = open(filename)
    except Exception:
      # 　没有网页
      responseHeaders = "HTTP/1.1 404 Not Found\r\n"
      responseHeaders += '\r\n'
      responseBody = "Sorry,Not found the page"
    else:
      # 　存在网页
      responseHeaders = "HTTP/1.1 200 OK\r\n"
      responseHeaders += '\r\n'
      responseBody = fd.read()
    finally:
      response = responseHeaders + responseBody
      connfd.send(response.encode())


if __name__ == "__main__":
  """
  希望通过HTTPServer类快速搭建http服务
　用以展示自己的网页
  """

  # 用户自己决定的内容
  HOST = '127.0.0.1'
  PORT = 8000
  DIR = "./static"  # 网页存储位置

  httpd = HTTPServer(HOST, PORT, DIR)  # 实例化对象
  httpd.serve_forever()  # 启动ｈｔｔｐ服务