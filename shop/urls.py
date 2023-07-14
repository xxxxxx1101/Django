from django.urls import path
from .views import author_list,book_list,movie_list,user,category

urlpatterns = [
    path ('author/',author_list,name='author_list'),
    path('book/',book_list,name = 'book_list'),
    path('movie/',movie_list, name='movie_list'),
    path('user/',user,name='user'),
    path('category/',category,name='category'),
]



