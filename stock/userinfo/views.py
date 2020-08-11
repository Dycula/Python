from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.db.models import ObjectDoesNotExist
from django.contrib.auth import authenticate,logout,login

from .models import UserInfo

import json
import logging
# Create your views here.
def SelfRegisterView(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        cpassword = request.POST.get("cpassword","")
        real_name = request.POST.get("realname","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        identify = request.POST.get("identify","")
        if username == "" or password =="" or cpassword == "":
            return HttpResponse(json.dumps({"result":False,"data":"","error":"用户名密码不能为空"}))
        old_user = UserInfo.objects.filter(username=username)
        if old_user:
            return HttpResponse(json.dumps({"result": False, "data": "", "error": "用户名已存在"}))
        if password != cpassword:
            return HttpResponse(json.dumps({"result": False, "data": "", "error": "两次密码不一致"}))
        password = make_password(password,None,"pbkdf2_sha1")
        try:
            new_user = UserInfo.objects.create(username=username,password=password,uemail=email,real_name=real_name,uphone=phone,uidentify=identify)
        except ObjectDoesNotExist as e:
            logging(e)
        return HttpResponse(json.dumps({"result": True, "data": "注册成功", "error": ""}))
    elif request.method == "GET":
        pass



def SelfLoginView(request):

    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        if username == "" or password == "":
            return HttpResponse(json.dumps({"result": False, "data": "", "error": "用户名密码不能为空"}))
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return HttpResponse(json.dumps({"result": True, "data": "登陆成功", "error": ""}))
        else:
            return HttpResponse(json.dumps({"result": False, "data": "", "error": "用户名密码错误"}))
    elif request.method == "GET":
        pass


def SelfLogoutView(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        logout(request)
        return HttpResponse(json.dumps({"result": True, "data": "注销成功", "error": ""}))