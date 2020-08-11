from flask import Flask

# 创建一个Flask的程序实例.以便接收用户的请求和响应
# 要将当前运行的模块文件作为Flask的程序示例
app = Flask(__name__)


# @app.route():Flask中的路由定义,用于匹配用户的访问路径，
# “/”表示整个网站的跟路径
# def index():匹配上路由之后要执行的操作函数
# 视觉函数（views）:视图函数中必须要返回一个字符串
@app.route("/index")
def index():
    return "hello world"


if __name__ == "__main__":
    # app.run:启动Flask的服务,默认会在本机开启5000端口
    # debug=True,可选参数,将启动模式改为调试模式
    app.run(debug=True)






