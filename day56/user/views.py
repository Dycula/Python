from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models


# Create your views here.
def login_view(request):
    #value = request.session.get("mypassword", "没有设置密码")
    if request.method == "GET":
        username = request.COOKIES.get("myname", "")
        return render(request, "user/login.html", locals())
    elif request.method == "POST":
        username = request.POST.get("username", "")
        if username == "":
            name_error = "请输入用户名！！"
            return render(request, "user/login.html", locals())
        password = request.POST.get("password", "")
        #request.session["mypassword"] = password
        remember = request.POST.get("remember", "")
        try:
            auser = models.User.objects.get(name=username, password=password)
        except:
            password_error = "用户名户密码不正确"
            return render(request, "user/login.html", locals())
        request.session["user"] = {"name": auser.username, "id": auser.id}

        #resp = HttpResponse("提交成功：remember=" + remember)
        resp=HttpResponseRedirect("/")

        if remember == "1":
            resp.set_cookie("myname", username,max_age=7*24*60*60)
        else:
            resp.delete_cookie("myname")
        return resp


def logout_view(requset):
    if "user" in requset.session:
        del requset.session["user"]
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect("/")


def reg_view(request):
    if request.method == "GET":
        return render(request, "user/reg.html", locals())
    elif request.method == "POST":
        username = request.POST.get("username", "")
        if username == "":
            name_error = "请输入用户名！！"
            return render(request, "user/reg.html", locals())
        password = request.POST.get("password", "")
        password2 = request.POST.get("password", "")
        if password != password2:
            password2_error = "俩次密码不一样"
            return render(request, "user/reg.html", locals())
        try:
            a_user = models.User.objects.get(username=username)
            name_error = "用户名已经存在"
            return render(request, "user/reg.html", locals())
        except:
            pass
        a_user = models.User.objects.create(username=username,password=password)
        html=username+"注册成功<a href='/user/login'>进入登录</a>"
        return HttpResponse(html)

from . import forms

def reg2_view(request):
    if request.method == "GET":
        reg2 =forms.Reg2()
        return render(request, "user/reg2.html", locals())
    elif request.method == "POST":
        form =forms.Reg2(request.POST)
        if form.is_valid():
            html=str(form.cleaned_data)
            return HttpResponse(html)
        else:
            return HttpResponse("你提交的数据不可用")


from django.views.generic.base import View
class Test(View):
    def get(self,request):
        print("---test------")
        return render(request,"test.html")
    def post(self,request):
        name=request.POST.get("name","")
        password=request.POST.get("password","")
        print(request.POST)
        return HttpResponse("name:"+name+"."+"password:"+password)



