from django.shortcuts import render, redirect
from django.http import HttpResponse
from goods.models import *
from cart.models import *
from models import *
from datetime import datetime
from django.db import transaction


def order(request):
    username = request.COOKIES.get('logined_username','')
    cart_id_list = request.GET.getlist('cid')
    cart_id_list = [int(i) for i in cart_id_list]
    cart_list = CartInfo.objects.filter(id__in=cart_id_list)
    print(cart_list)
    context = {'username': username, 'cart_list': cart_list}
    return render(request, 'order/place_order.html', context)


@transaction.atomic
def create_order(request):
    sid = transaction.savepoint()
    try:
        username = request.COOKIES.get('logined_username')
        user = UserInfo.objects.filter(user=username)[0]
        now = datetime.now()
        oid = now.strftime('%Y%m%d%H%M%S') + str(user.id)
        address = request.GET.get('address')
        cart_id_list = request.GET.getlist('cid')
        cart_list = CartInfo.objects.filter(id__in=cart_id_list)
        zongjia = 0
        for i in cart_list:
            xiaoji = i.count * i.good.gprice
            zongjia += xiaoji

        orderinfo = OrderInfo()
        orderinfo.user = user
        orderinfo.id = oid
        orderinfo.time = now
        orderinfo.address = address
        orderinfo.total = zongjia
        orderinfo.save()

        for i in cart_list:
            orderdetail = OrderDetail()
            orderdetail.count = i.count
            orderdetail.xiaoji = i.count * i.good.gprice
            orderdetail.good = i.good
            orderdetail.price = i.good.gprice
            orderdetail.order = orderinfo
            orderdetail.save()

            i.good.gkucun -= i.count
            if i.good.gkucun < 0:
                raise Exception
            i.good.save()
            i.delete()

    except Exception as e:
        transaction.savepoint_rollback(sid)
        print(e)
    else:
        transaction.savepoint_commit(sid)

    return redirect('/user_center/user_center_order/')