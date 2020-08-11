from django.conf.urls import url
from . import views

urlpatterns = [

  url(r'^/(?P<topic_id>[\d]+)$', views.messages, name='messages')

]