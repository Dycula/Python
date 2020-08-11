from django.shortcuts import render
def show_image(request):
    return render(request,"show_image.html",locals())