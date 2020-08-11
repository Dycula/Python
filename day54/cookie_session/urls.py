from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^set_cookies",views.set_cookie),
    url(r"^get_cookies",views.get_cookie),
]