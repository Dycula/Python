# tornado读取客户端上传文件并存储
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
        #利用request对象
        #获得客户端提交的文件内容
        files=self.request.files
        avatars=files.get("avatar")
        for avatar in avatars:
            filename=avatar.get("filename")
            print("filename",filename)
            ext=avatar.get("content_type")
            print("文件类型",ext)
            data=avatar.get("body")#二进制格式的文件内容
            #把内容进行保存(往磁盘上保存)
            writer=open("upload/%s"%filename,"wb")
            writer.write(data)
            writer.close()
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
