from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
from user.models import User


# Create your views here.
# 函数装饰器检测用户是否登录,如果没有登录则直接跳转到登录界面
def check_login(fn):
    def wrap(request, *args, **kwargs):
        if "user" not in request.session:
            return HttpResponseRedirect("/user/login")
        else:
            return fn(request, *args, **kwargs)

    return wrap


def add_view(request):
    if "user" not in request.session:
        return HttpResponseRedirect("/user/login")
    if request.method == "GET":
        return render(request, "note/add_note.html")
    elif request.method == "POST":
        try:
            a_user = User.objects.get(id=request.session["user"]["id"])
        except:
            return HttpResponse("登录用户数据错误")
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        # 根据表单内容创建记录
        models.Note.objects.create(title=title, content=content, user=a_user)
        return HttpResponseRedirect("/note/")

from django.core.paginator import Paginator
@check_login
def list_view(request):
    try:
        a_user_id = request.session["user"]["id"]
        a_user = User.objects.get(id=a_user_id)
    except:
        return HttpResponse("失败")
    notes = a_user.note_set.all()
    #return render(request, "/note/list_note.html", locals())

    paginator=Paginator(notes,5)#把notes以每页５条进行分类
    print("分页前的数据个数：",Paginator.count)
    print("分页前的数据个数：",Paginator.num_pages)
    #先得到当前的页码信息,如果没有？page=xxx,返回第一页信息
    page_number=request.GET.get()
    page=paginator.page()
    return render(request,"note/list_note2.html",locals())



@check_login
def del_view(request, id):
    try:
        a_user_id = request.session["user"]["id"]
        a_user = User.objects.get(id=a_user_id)
    except:
        return HttpResponse("失败")
    a_note = a_user.note_set.get(id=id)
    a_note.delete()
    return HttpResponseRedirect("/note/")


@check_login
def mod_view(request, id):
    try:
        a_user_id = request.session["user"]["id"]
        a_user = User.objects.get(id=a_user_id)
    except:
        return HttpResponse("失败")
    a_note = a_user.note_set.get(id=id)
    if request.method == "GET":
        return render(request, "note/mod_note.html", locals())
    elif request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        a_note.title = title
        a_note.content = content
        a_note.save()
        return HttpResponseRedirect("/note/")
