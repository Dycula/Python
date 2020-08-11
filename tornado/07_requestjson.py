# tornado读取客户端以json字符串提交的字符串数据的信息
#json字符串：{"key1":"value1","key2":"value2"}
import json

from tornado.options import define, options, parse_config_file
from tornado.web import Application, RequestHandler

import tornado

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


# 用来响应用户请求
class IndexHandler(RequestHandler):
    # 响应以get方式发起请求
    def get(self, *args, **kwargs):
        # 服务器给浏览器的响应内容
        self.write("hello tornado")

    # 响应以post方式发起的请求
    def post(self, *args, **kwargs):
        #利用request属性
        #取出客户端提交的json字符串
        jsonbyte=self.request.body
        print("二进制格式json字符串：",jsonbyte)
        jsonstr=jsonbyte.decode("utf8")
        print("json字符串：",jsonstr)
        #json字符串转换为json对象,然后利用json对象提供的api
        #从json字符串中取出想要的内容(解析json字符串)
        jsonobj=json.loads(jsonstr)
        day=jsonobj.get("day")
        title=jsonobj.get("title")
        print("day:",day,"title:",title)
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
