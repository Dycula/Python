import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from .models import Users


# Create your views here.
def create_view(requset):
    return render(requset, "createXhr.html")


def server_view(request):
    return HttpResponse("这是server的响应内容")


def get_view(request):
    return render(request, "get.html")


def getparans_view(request):
    return render(request, "getparans.html")


def serverparans_view(request):
    # 接收前端传递过来的俩个参数
    name = request.GET["name"]
    age = request.GET["age"]
    # 响应数据给前端
    s = "姓名：%s,年龄：%s" % (name, age)
    return HttpResponse(s)


def register_view(request):
    return render(request, "register.html")


def check_view(request):
    # 接收前端传递过来的参数
    uname = request.GET["uname"]
    # 判断uname在users实体中是否存在查询操作
    users = Users.objects.filter(uname=uname)
    # 根据查询结构给出响应
    if users:
        return HttpResponse("1")
    return HttpResponse("0")


def result_view(request):
    # 接收前端传递的数据
    uname = request.GET["uname"]
    upwd = request.GET["upwd"]
    uemail = request.GET["uemail"]
    nickname = request.GET["nickname"]
    # 通过实体类实现增加操作(通过异常处理增加失败的问题)
    try:
        Users.objects.create(uname=uname, upwd=upwd,
                             uemail=uemail, nickname=nickname)
        return HttpResponse("1")
    except Exception as e:
        print(e)
        return HttpResponse("0")


def result01_view(request):
    # 接收前端传递的数据
    uname = request.POST["uname"]
    upwd = request.POST["upwd"]
    uemail = request.POST["uemail"]
    nickname = request.POST["nickname"]
    # 通过实体类实现增加操作(通过异常处理增加失败的问题)
    try:
        Users.objects.create(uname=uname, upwd=upwd,
                             uemail=uemail, nickname=nickname)
        return HttpResponse("1")
    except Exception as e:
        print(e)
        return HttpResponse("0")


def post_view(request):
    return render(request, "post.html")


def postparans_view(request):
    uname = request.POST["uname"]
    upwd = request.POST["upwd"]
    msg = "用户名：%s,密码：%s" % (uname, upwd)
    return HttpResponse(msg)


def users_view(request):
    return render(request, "users.html")


def users_server_view(requset):
    users = Users.objects.all()
    msg = ""
    for u in users:
        msg += "%s_%s_%s_%s_%s" % (u.id, u.uname, u.upwd, u.uemail, u.nickname)
    msg = msg[0:-1]
    return HttpResponse(msg)


def json_view(request):
    return render(request, "json.html")


def json_server(request):
    # 1.使用字典表示json数据
    # dic={
    #     "course":"Ajax",
    #     "duration":3,
    #     "place":"beijing"
    # }
    # 将dic通过json.dumps转换程json格式的字符串
    # jsonStr=json.dumps(dic)

    # 2.使用列表表示多个json数据(列表封装字典)
    list = [
        {"course": "Ajax", "duration": 3, "place": "beijing"},
        {"course": "Java", "duration": 4, "place": "shenzhen"},
        {"course": "Python", "duration": 5, "place": "guangzhou"}
    ]
    jsonStr = json.dumps(list)
    return HttpResponse(jsonStr)


def json_users(request):
    users = Users.objects.all()
    # jsonUsers=json.dumps(users)#QuerySet不支持json
    jsonUsers = serializers.serialize("json", users)
    return HttpResponse(jsonUsers)


def jsonusers_view(request):
    return render(request, "jsonusers.html")


def jsonusers_server_view(request):
    users = Users.objects.all()
    jsonUsers = serializers.serialize("json", users)
    return HttpResponse(jsonUsers)


def frontjson_view(request):
    return render(request, "frontjson.html")


def serverjson_view(request):
    jsonStr = '{"uname":"wang","uage":25,"ugender":"男"}'
    # 通过json.loads()将jsonStr转换成python字典
    dic = json.loads(jsonStr)
    s = "姓名：%s,年龄：%s,性别：%s" % (dic["uname"], dic["uage"], dic["ugender"])
    return HttpResponse(s)


def registerjson_view(requset):
    return render(requset, "registerjson.html")


def registerjson_server_view(requset):
    params = requset.GET["params"]
    # 将params封装成python字典
    dic = json.loads(params)
    try:
        Users.objects.create(uname=dic["uname"], upwd=dic["upwd"], uemail=dic["uemail"], nickname=dic["nickname"])
        return HttpResponse("注册成功")
    except Exception as e:
        print(e)
        return HttpResponse("注册失败")


def head_view(request):
    return render(request, "head.html")


def index_view(request):
    return render(request, "index.html")


def jqueryget_view(request):
    return render(request, "jqueryget.html")


def search_view(request):
    return render(request,"search.html")


def jqueryserver_view(request):
    #接收前端产地过来的参数--kw
    kw=request.GET["kw"]
    #查询Users实体中uname列中包含kw的信息
    users=Users.objects.filter(uname__contains=kw)
    #将uname封装成列表在转换成JSON串响应
    uList=[]
    if users:
        for u in users:
            uList.append(u.uname)
    return HttpResponse(json.dumps(uList))



def jqueryajax_view(request):
    return render(request,"jqueryajax.html")