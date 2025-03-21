from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blogpost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def blog_list(request):
    posts = Blogpost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})


