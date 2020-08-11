from tornado.ioloop import IOLoop

from tornado.httpserver import HTTPServer
from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        html = "<form method=post action=/login enctype=multipart/form-data>" \
               "<input type=text name=name><br><br>" \
               "<input type=password name=password><br><br>" \
               "<input type=file name=avatar><br><br>" \
               "<input type=submit value=提交>&nbsp;&nbsp;" \
               "<input type=reset value=重置>&nbsp;&nbsp;" \
               "</form>"
        self.write(html)

    def post(self, *args, **kwargs):
        pass


define("port", default=8888, type=int, multiple=False)
parse_config_file("09_config")


class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        name = self.get_body_argument("name",None)
        password = self.get_body_argument("password",None)
        print("用户名：", name, ",密码：", password)
        files=self.request.files
        #明确知道用户就上传了一张图片时
        #用下标的方式将唯一一张图片直接取出
        avatar=files.get("avatar")[0]
        filename=avatar.get("filename")
        body=avatar.get("body")
        writer=open("upload/%s"%filename,"wb")
        writer.write(body)
        writer.close()


app = Application([("/", IndexHandler),
                   ("/login", LoginHandler)
                   ])
server = HTTPServer(app)
server.listen(options.port)
print(options.port)
IOLoop.current().start()
