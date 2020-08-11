# 演示tornado页面间跳转
from tornado.ioloop import IOLoop

from tornado.httpserver import HTTPServer
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler

# 模块级别的变量　　访问（读/写）
# 被遮蔽了
IS_SUCCESS = True


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        html = "<form method=post action=/login enctype=multipart/form-data>" \
               "<input type=text name=name><br></br>" \
               "<input type=password name=password><br></br>" \
               "<input type=submit value=提交>&nbsp;&nbsp;" \
               "<input type=reset value=重置>&nbsp;&nbsp;" \
               "</form>"
        self.write(html)
        # if not IS_SUCCESS:
        #     self.write("<br></br>")
        #     self.write("<span>用户名或密码错误</span>")
        msg = self.get_query_argument("msg", None)
        if msg:
            self.write("<br></br>")
            self.write("<span>用户名或密码错误</span>")

    def post(self, *args, **kwargs):
        pass


define("port", default=8888, type=int, multiple=False)
parse_config_file("09_config")


class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        name = self.get_body_argument("name", None)
        password = self.get_body_argument("password", None)
        print("用户名：", name, ",密码：", password)
        # files=self.request.files
        # #明确知道用户就上传了一张图片时
        # #用下标的方式将唯一一张图片直接取出
        # avatar=files.get("avatar")[0]
        # filename=avatar.get("filename")
        # body=avatar.get("body")
        # writer=open("upload/%s"%filename,"wb")
        # writer.write(body)
        # writer.close()
        if name == "abc" and password == "123":
            # 如果输入的用户名和密码正确,则跳转到博客页面
            # IS_SUCCESS=True
            self.redirect("/blog")
        else:
            # 否则重新输入用户名和密码再次登录
            # IS_SUCCESS=False
            self.redirect("/?msg=fail")


class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("welcome blog")

    def post(self, *args, **kwargs):
        pass


app = Application([("/", IndexHandler),
                   ("/login", LoginHandler),
                   ("/blog", BlogHandler)
                   ])
server = HTTPServer(app)
server.listen(options.port)
print(options.port)
IOLoop.current().start()
