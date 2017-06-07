# coding:utf-8
from django.shortcuts import render, redirect
from models import *
from django.http import HttpResponse
from goods.models import *
# Create your views here.

def index(request):
    logined_username = request.COOKIES.get('logined_username', '')
    context = {'username': logined_username}
    return render(request, 'goods/index.html', context)

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
    if not userinfo:
        return HttpResponse('fault username')

    if pwd == userinfo[0].pwd:
        response = HttpResponse('login success')
        response.set_cookie('logined_username', user_name, 18000)
        return response
    else:
        return HttpResponse('fault password')

def user_center_info(request):
    lately = request.COOKIES.get('lately','')
    if lately == '':
        lately_list = []
    else:
        lately_list = lately.split(',')
    for i in range(len(lately_list)):
        if lately_list[i] != '':
            lately_list[i] = int(lately_list[i])
        else:
            lately_list.remove(lately_list[i])
    lately_goods_list = []
    for i in lately_list:
        goodinfo = GoodsInfo.objects.get(id=i)
        lately_goods_list.append(goodinfo)

    user = request.COOKIES.get('logined_username', 'moren')
    userinfo = UserInfo.objects.filter(user=user)
    if userinfo:
        userinfo = userinfo[0]
        address = userinfo.address
        tel = userinfo.tel
        postcode = userinfo.postcode
        receiver = userinfo.receiver
        context = {'username': user, 'receiver': receiver, 'address': address, 'tel': tel, 'postcode': postcode, 'lately': lately_goods_list}
    else:
        return redirect('/user_center/login/')
    return render(request, 'user_center/user_center_info.html', context)

def user_center_order(request):
    logined_username = request.COOKIES.get('logined_username', '')
    context = {'username': logined_username}
    return render(request, 'user_center/user_center_order.html', context)

def user_center_site(request):
    user = request.COOKIES.get('logined_username', 'moren')
    userinfo = UserInfo.objects.filter(user=user)
    if userinfo:
        userinfo = userinfo[0]
        address = userinfo.address
        tel = userinfo.tel
        postcode = userinfo.postcode
        receiver = userinfo.receiver
        context = {'username': user, 'receiver': receiver, 'address': address, 'tel': tel, 'postcode': postcode}
    else:
        return redirect('/user_center/login/')
    return render(request, 'user_center/user_center_site.html', context)

def user_center_site_submit(request):
    address = request.POST.get('address')
    receiver = request.POST.get('receiver')
    postcode = request.POST.get('postcode')
    tel = request.POST.get('tel')
    user = request.COOKIES.get('logined_username')
    userinfo = UserInfo.objects.get(user=user)
    userinfo.address = address
    userinfo.receiver = receiver
    userinfo.postcode = postcode
    userinfo.tel = tel
    userinfo.save()
    return redirect('/user_center/user_center_site/')

def quit(request):
    response = render(request, 'goods/index.html')
    response.set_cookie('logined_username', '', -1)
    return response