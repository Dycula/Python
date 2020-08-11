from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import models


def set_cookie(requset):

     return HttpResponse("OK")
     resp.set_cookie("aaa","bbb")
     return resp



def get_cookie(requset):

    return HttpResponse("ok")
