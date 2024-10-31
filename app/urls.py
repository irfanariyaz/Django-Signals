from django.urls import path,include
from .views import index, blog_list



urlpatterns = [
    path('', index, name='index'),  # Homepage with the form
    path('blogs/', blog_list, name='blog_list'),  # Page to view the list of blogs
]