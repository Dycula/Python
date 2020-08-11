from django.http import HttpResponse

"""
def page1_view(request):
    html = "欢迎来到第一个页面"
    html += "<a href='www.baidu.com'>百度一下</a>"
    html += "<a href='/'>返回首页</a>"
    return HttpResponse(html)


def index_view(request):
    html = "hello"
    html += "跳转到<a href='/page1'>第一页</a>"
    return HttpResponse(html)


def frist(request):
    html = "这是我的首页"
    html += "跳转到<a href='/page2'>第一页</a>"
    html += "<a href='/'>返回首页</a>"
    return HttpResponse(html)


def page1(request):
    html = "这是我的１页"
    html += "跳转到<a href='/page1'>第一页</a>"
    return HttpResponse(html)


def page2(request):
    html = "这是我的２页"
    html += "跳转到<a href='/page2'>第二页</a>"
    return HttpResponse(html)


def year_view(request, y):
    html = "URL中的年份是：" + y
    return HttpResponse(html)


def fun(request, a, op, b):
    a = int(a)
    b = int(b)
    if op == "add":
        return HttpResponse(str(a + b))
    elif op == "sub":
        return HttpResponse(str(a - b))
    elif op == "mul":
        return HttpResponse(str(a * b))
    else:
        return HttpResponse("错误")


def date_view(request, y, m, d):
    html = y + "年" + m + "月" + d + "日"
    return HttpResponse(html)


def show_info(request):
    html = "request.path" + request.path
    if request.method == "GET":
        html += "<h6>正在进行GET请求</h6>"
    elif request.method == "POST":
        html += "<h6>正在进行POST请求</h6>"
        html += "<h6>ip地址是：" + request.META["REMOTE_ADDR"]
    return HttpResponse(html)


def page_view(request):
    html = ""
    if request.method == "GET":
        dic = dict(request.GET)
        s = str(dic)
        html += "GET请求：" + s
        b = request.GET.get("b", "没有值！")
        html += "<br>" + b
    elif request.method == "POST":
        pass
    return HttpResponse(html)

"""
def sum_view(requset):
    if requset.method == "GET":
        start = requset.GET.get("start", "0")
        stop = requset.GET["stop"]
        step = requset.GET.get("step", "1")
        start, stop, step = int(start), int(stop), int(step)
        result = sum(range(start, stop, step))
    return HttpResponse("结果是:%d" % result)
