from django.conf.urls import url
from .views import SelfRegisterView,SelfLoginView, SelfLogoutView

urlpatterns = [
    url(r'myregister/', SelfRegisterView,name="myregister"),
    url(r'mylogin/', SelfLoginView,name="mylogin"),
    url(r'mylogout/', SelfLogoutView,name="mylogout"),
]
