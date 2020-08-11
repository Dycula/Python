from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render
class Test(View):
    def get(self,request):
        print("---test------")
        return render(request,"test.html")
    def post(self,request):
        name=request.POST.get("name","")
        password=request.POST.get("password","")
        print(request,POST)
        return HttpResponse("name:"+name+"."+"password:"+password)

