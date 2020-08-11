"""
请求HttpRequest
响应HttpResponse
def xxx_view(request):
    if request.method=="GET":
        return HttpRequest("GET")
    elif request.method=="POST":
        return HttpResponse("POST")
get请求：
request.GET(QueryDict类型的字段)
request.GET["key"]
request.GET.get("key","默认值")
requset.GET.getlist("key")
Post请求
request.POST(QueryDict类型的字段)
request.POST["key"]
request.POST.get("key","默认值")
requset.POST.getlist("key")
"""
"""
Django遵循的设计模式
MVC模式
M-model
V-view
C-controller

MTV模式
M-model
T-template
V-view

"""