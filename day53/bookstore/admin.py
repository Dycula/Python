from django.contrib import admin

# Register your models here.
from . import models


class BookManage(admin.ModelAdmin):#编写模型管理区类
    list_display = ["id","title","pub","price","pub_date"]
    list_display_links = ["id","title","pub"]
    list_filter = ["pub"]
    search_fields = ["title","pub"]
    list_editable = ["price"]




admin.site.register(models.Book,BookManage)
admin.site.register(models.Author)
admin.site.register(models.wife)
