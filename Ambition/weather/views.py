from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def mysql_view(request):
    return render(request,"mysql.html")

