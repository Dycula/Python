from django.conf.urls import url
from . import views

urlpatterns = [
  #http://127.0.0.1:8000/v1/topics/<author_id>
  url(r'^/(?P<author_id>[\w]+)$', views.topics, name='topics')
]