# tornado读取客户端提交的访问参数
from tornado.options import define, options, parse_config_file
from tornado.web import Application, RequestHandler

import tornado

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


# 用来响应用户请求
class IndexHandler(RequestHandler):
    # 响应以get方式发起请求
    def get(self, *args, **kwargs):
        #第一种方式处理不传参数的方式
        # try:
        #     arg=self.get_query_argument("day")
        # except Exception as e:
        #     arg=None
        #第二种方式处理不传参数的方式
        arg = self.get_query_argument("day",None)
        print("arg--->",arg)
        args=self.get_query_arguments("day")
        print("args--->", args)
        # 服务器给浏览器的响应内容
        self.write("hello tornado")

    # 响应以post方式发起的请求
    def post(self, *args, **kwargs):
        arg=self.get_body_argument("day",None)
        print("post的方式获取的arg",arg)
        args=self.get_body_arguments("day")
        print("post的方式获取的args", args)

        #get_argument=get_query_argument+get_body_argument
        arg2=self.get_argument("day")
        print("get_argument获取的arg:",arg2)
        arg2s=self.get_arguments("day")
        print("get_argument获取的args:",arg2s)
        #利用requestHandler中的一个属性request
        #获取请求头中感兴趣的内容
        #Content-Type ,myheader,yourheader
        head=self.request.headers
        print("head的类型：",type(head))
        ct=head.get("Content-Type",None)
        mh=head.get("myheader",None)
        yh=head.get("yourheader",None)
        print("Content-Type",ct)
        print("myheader",mh)
        print("yourheader",yh)
        self.write("hello post")


# 定义一个变量,用来代表端口号
define("port", type=int, default=8888, multiple=False)
#定义一个变量,用来代表数据库的连接信息(用户名,密码,端口号,数据库名称)
define("db",multiple=True,type=str,default=[])
# 从指定的配置文件中,读取port的内容
parse_config_file("02_config")
# 创建Application对象,进行若干个对服务器的设置　
# 例如：路由列表,模板路径,静态资源路径
app = Application([("/", IndexHandler)])
# 创建服务器程序
server = HTTPServer(app)
# 服务器监听某个端口
server.listen(options.port)
#打印获得的数据库参数
print("数据库参数：",options.db)
# 启动服务器(在当期进程中启动服务器)
IOLoop.current().start()
