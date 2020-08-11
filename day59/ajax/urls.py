from django.conf.urls import url
from . import  views
urlpatterns=[
    #演示创建xhr
    url(r"^show/$",views.create_view),

    #演示使用ajax发送get请求的步骤
    url(r"^server/$",views.server_view),
    url(r"^get/$",views.get_view),

    #演示使用ajax发送get请求并附带参数
    url(r"^getparans/$",views.getparans_view),
    url(r"^serverparans/$",views.serverparans_view),

    #使用ajax完成注册操作
    url(r"^register/$",views.register_view),
    url(r"^check$",views.check_view),
    url(r"^result/$",views.result_view),
    url(r"^result01/$",views.result01_view),

    #使用ajax发送post请求
    url(r"^post/$",views.post_view),
    url(r"^server01/$",views.postparans_view),

    #使用ajax读取数据
    url(r"^users/$",views.users_view),
    url(r"^users_server/$",views.users_server_view),

    #在前端中处理JSON格式字符串
    url(r"^json/$",views.json_view),

    #在服务器端处理JSON字符串
    url(r"^json_server/$",views.json_server),

    #在服务器端中读取users表中的数据再转换成JSON
    url(r"^json_users",views.json_users),

    #读取Uesrs信息并显示在网页上(json)
    url(r"^jsonusers/$",views.jsonusers_view),
    url(r"^jsonusers_server/$",views.jsonusers_server_view),

    #前端中将json对象转换成json串
    url(r"^frontjson/$",views.frontjson_view),
    url(r"^serverjson/$",views.serverjson_view),

    #通过json完成注册操作
    url(r"^registerjson/$",views.registerjson_view),
    url(r"^registerjson_server/$",views.registerjson_server_view),

    #演示jquery中的$obj.load()的作用
    url(r"^head/$",views.head_view),
    url(r"^index/$",views.index_view),

    #显示jquery中的$get()的作用
    url(r"^jqueryget/$",views.jqueryget_view),

    #通过$.get()完成搜索建议
    url(r"^search/$",views.search_view),
    url(r"^jqueryserver/$",views.jqueryserver_view),

    #通过$.ajax()完成自定义的ajax的请求
    url(r"^jqueryajax/$",views.jqueryajax_view),
]