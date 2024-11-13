# books/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'), 
    path('add/', views.add_book, name='add_book'),
    path('books/', views.book_list, name='book_list'),
]
