from django.urls import path
from .views import blog_list
from .import views

urlpatterns = [
    path('', blog_list, name='blog_list'),
]