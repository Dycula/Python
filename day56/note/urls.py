from django.conf.urls import url
from . import views
urlpatterns=[
    url(r"^add",views.add_view),#添加
    url(r"^$",views.list_view),#查看
    url(r"^del/(\d+)",views.del_view),#删除
    url(r"^mod/(\d+)",views.mod_view),#修改
]