"""day51 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^page1$', views.page1_view),
    # url(r"^$", views.index_view),
    # url(r"^$", views.frist),
    # url(r"^page1$", views.page1),
    # url(r"^page2$", views.page2),
    # url(r"^year/(\d{4})$", views.year_view),
    # url(r"^(\d)(\w{3})(\d)$", views.fun),
    # url(r"^date/(\d{4})/(\d{1,2})/(\d{1,2})$", views.date_view),
    # url(r"^show_info$", views.show_info),
    # url(r"^page", views.page_view),
    url(r"^sum$", views.sum_view),
]
