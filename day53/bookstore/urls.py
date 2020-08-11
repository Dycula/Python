

# file bookstore/urls.py


from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^add$', views.add_book_view),
    url(r'^books$',views.books_view),
    url(r'^add2$',views.book_add2_view),
]