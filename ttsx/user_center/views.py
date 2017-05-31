# coding:utf-8
from django.shortcuts import render, redirect
from models import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'user_center/index.html')

def register(request):
    return render(request, 'user_center/register.html')

def register2(request):
    post = request.POST
    user_name = post.get('user_name')
    pwd = post.get('pwd')
    email = post.get('email')

    userinfo = UserInfo()
    userinfo.user = user_name
    userinfo.pwd = pwd
    userinfo.mail = email
    userinfo.save()
    return redirect('/index/')

def is_registed(request):
    get_name = request.GET.get('user_name')
    a = UserInfo.objects.filter(user=get_name)
    if a:
        return HttpResponse('exist')
    else:
        return HttpResponse('not exist')

def login(request):
    return render(request, 'user_center/login.html')

def login2(request):
    gets = request.GET
    user_name = gets.get('username')
    pwd = gets.get('pwd')

    userinfo = UserInfo.objects.filter(user=user_name)
    print(userinfo)
    if not userinfo:
        return HttpResponse('fault username')

    if pwd == userinfo[0].pwd:
        return HttpResponse('login success')
    else:
        return HttpResponse('fault password')




