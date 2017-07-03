from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from user_center.models import *
from goods.models import *
from cart.models import *


def cart(request):
    username = request.COOKIES.get('logined_username', '')
    if username == '':
        return redirect('/user_center/login/')

    user = UserInfo.objects.filter(user=username)
    userid = user[0].id
    carts = CartInfo.objects.filter(user__id=userid)
    context = {'carts': carts, 'username': username}
    return render(request, 'cart/cart.html', context)


def add(request):
    username = request.COOKIES.get('logined_username', '')
    if username == '':
        return redirect('/user_center/login/')
    count = request.GET.get('count', '1')
    user = UserInfo.objects.filter(user=username)
    gid = request.GET.get('gid', '1')
    good = GoodsInfo.objects.filter(id=int(gid))

    if good and user:
        cartinfo = CartInfo.objects.filter(user=user[0]).filter(good=good[0])
        if cartinfo:
            cartinfo[0].count = str(int(cartinfo[0].count) + int(count))
            cartinfo[0].save()
        else:
            cartinfo = CartInfo()
            cartinfo.user = user[0]
            cartinfo.count = count
            cartinfo.good = good[0]
            cartinfo.save()
        return redirect('/cart/')
    else:
        return HttpResponse('cart error')

def get_count(request):
    username = request.COOKIES.get('logined_username', '')
    userinfo = UserInfo.objects.filter(user=username)
    if userinfo:
        count = CartInfo.objects.filter(user=userinfo[0]).count()
        return JsonResponse({'count': count})
    else:
        return JsonResponse({'count': 0})

def delete(request):
    cid = request.GET.get('cid')
    cid = int(cid)
    print(cid)
    cartinfo = CartInfo.objects.get(id=cid)
    cartinfo.delete()
    return HttpResponse('ok')

def update(request):
    cid = request.GET.get('cid')
    count = request.GET.get('count')
    cartinfo = CartInfo.objects.filter(id=cid)
    if cartinfo:
        cartinfo[0].count = count
        cartinfo[0].save()
    return HttpResponse('ok')

