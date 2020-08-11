from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index$', views.homepage),
    url(r"^mysql$",views.mysql_view),
]