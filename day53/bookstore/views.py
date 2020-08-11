from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import models


def add_book_view(request):
    if request.method == 'GET':
        btitle = request.GET.get('title', 'No Name')
        bpub = request.GET.get('pub', '')
        # 方法1  创建一条记录
        # book = models.Book.objects.create(title=btitle,
        #                            pub=bpub)
        # 方法2
        book = models.Book()  # 创建实例
        book.title = btitle
        book.pub = bpub
        book.price = 99.9
        import datetime
        # book.pub_date = datetime.datetime(2008,1,1).date() #'2008-1-1'  # 或datetime类型
        book.pub_date = '2008-1-2'  # 或datetime类型
        book.save()  # 执行SQL语句
        print(book)
        return HttpResponse("添加成功!!!")


def books_view(requset):
    books = models.Book.objects.all()
    return render(requset, "books.html", locals())


def book_add2_view(request):
    if request.method == "GET":
        return render(request, "bookinfo.html")
    elif request.method == "POST":
        title = request.POST.get("tilte", "")
        pub = request.POST.get("pub", "")
        price = request.POST.get("price", "0.0")
        market_price = request.POST.get("market_price", "0.0")
        try:
            abook = models.Book.objects.create(
                title=title,
                pub=pub,
                price=price,
                market_price=market_price
            )
            return HttpResponseRedirect("/bookstore/books")
        except:
            return HttpResponse("添加失败")
