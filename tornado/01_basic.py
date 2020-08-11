#ALT+ENTER快捷导入模块
#ctrl+Y删除一行
from tornado.web import Application, RequestHandler

import tornado

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

#用来响应用户请求
class IndexHandler(RequestHandler):
    #响应以get方式发起请求
    def get(self,*args,**kwargs):
        #服务器给浏览器的响应内容
        self.write("hello tornado")
    #响应以post方式发起的请求
    #响应以post方式发起的请求
    def post(self,*args,**kwargs):
        pass

#创建Application对象,进行若干个对服务器的设置　
# 例如：路由列表,模板路径,静态资源路径
app=Application([("/",IndexHandler)])
#创建服务器程序
server=HTTPServer(app)
#服务器监听某个端口
server.listen(8888)
#启动服务器(在当期进程中启动服务器)
IOLoop.current().start()







