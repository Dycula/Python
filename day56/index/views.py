from django.shortcuts import render
from django.http import HttpResponse
#导入setting模块
from django.conf import settings
import os
# Create your views here.
def index_view(request):
    return render(request,"index/index.html",locals())




def upload_view(request):
    if request.method=="GET":
        return render(request,"index/upload.html",locals())
    elif request.method=="POST":
        #此时可以通过request.FILES未获取上传的文件
        a_file=request.FILES["myfile"]
        #此处保存上传的文件到"static/files"文件夹内
        filename=os.path.join(settings.MEDIA_ROOT,a_file.name)
        with open(filename,"wb") as f:
            #a_file绑定一个已经打开的文件流对象
            data=a_file.file.read()
            f.write(data)
        return HttpResponse("文件"+a_file.name+"上传成功")