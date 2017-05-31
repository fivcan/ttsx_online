from django.shortcuts import render
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

    return HttpResponse('ok')
