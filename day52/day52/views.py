from django.http import HttpResponse

html = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/test_post" method="post">
        <input type="text" name="search_name">
        <input type="text" name="name2">
        <select name="gender">
            <option value=1> </option>
            <option value=0> </option>
        </select>
        <textarea name="comment" rows="5" cols="10">...</textarea>
        <input type="submit" value="开始搜索">
    </form>
</body>
</html>
'''


def test_post_view(request):
    if request.method == "GET":
        return HttpResponse(html)
    if request.method == "POST":
        value = request.POST['search_name']
        dic = dict(request.POST)
        return HttpResponse("search_name=" + value + str(dic))


"""
from django.template import loader


def test1_view(request):
    # 绑定模板对象
    t = loader.get_template("myhomepage.html")
    # 用模板生成html
    html = t.render()
    # 返回给浏览器
    return HttpResponse(html)
"""

from django.shortcuts import render


def test2_view(request):
    person = {"name": "tedu", "age": 18}
    return render(request, "myhomepage.html", person)


def page1_view(request):
    myvar = 999
    mystr = "hello world"
    mylist = ["深圳", "北京"]
    person = {"name": "tedu", "age": 18}

    def myfun1():
        return "函数结果"

    money = 167865841657496

    city = ["北京", "上海", "深圳"]
    return render(request, "page1.html", locals())


def page2_view(request):
    return render(request, "page2.html")


def page3_view(request):
    return render(request, "page3.html")


def page4_view(request):
    return render(request, "page4.html")


def pagen_view(request,n):
    return render(request, "pagen.html", locals())
