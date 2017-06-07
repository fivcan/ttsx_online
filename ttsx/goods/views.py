from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from models import *
from django.core.paginator import Paginator


def index(request):
    logined_username = request.COOKIES.get('logined_username', '')
    context = {'username': logined_username}
    return render(request, 'goods/index.html', context)


def json_index(request):
    new_goods_list = []
    for i in range(6):
        new_goods_list.append(i)
        new_goods = GoodsInfo.objects.filter(gtype_id=i+1).order_by('-id')[0:3]
        new_goods_list[i] = []
        for j in new_goods:
            new_goods_list[i].append({"gtitle": j.gtitle, "gpic": j.gpic.name, "gprice": j.gprice, 'gid': j.id})

    popularity_goods_list = []
    for i in range(6):
        popularity_goods_list.append(i)
        new_goods = GoodsInfo.objects.filter(gtype_id=i + 1).order_by('-gclick')[0:3]
        popularity_goods_list[i] = []
        for j in new_goods:
            popularity_goods_list[i].append({"gtitle": j.gtitle, 'gid': j.id})

    return JsonResponse({'new_goods_list': new_goods_list, 'popularity_goods_list': popularity_goods_list})


def detail(request):
    username = request.COOKIES.get('logined_username')
    gid = request.GET.get('gid')
    lately = request.COOKIES.get('lately', '')
    lately_list = lately.split(',')
    if str(gid) in lately_list:
        lately_list.remove(str(gid))
    lately_list.insert(0, str(gid))
    if len(lately_list) > 5 :
        lately_list.pop()
    str_lately = ','.join(lately_list)
    goodsinfo = GoodsInfo.objects.filter(id=gid)
    if goodsinfo:
        tid = goodsinfo[0].gtype_id
        type_name = TypeInfo.objects.get(id=tid).ttitle
        goodsinfo[0].gclick += 1
        goodsinfo[0].save()
        recommand = GoodsInfo.objects.filter(gtype_id=tid).order_by('-id')[0:2]
        context = {'recommand':recommand, 'good': goodsinfo[0], 'type_name': type_name, 'username': username}
    else:
        context = {}
    response = render(request, 'goods/detail.html', context)
    response.set_cookie('lately', str_lately)
    return response


def goods_more(request):
    page_num = request.GET.get('page', '1')
    tid = request.GET.get('tid', '1')
    sort = request.GET.get('sort', '1')
    try:
        type_name = TypeInfo.objects.filter(id=tid)[0].ttitle
    except:
        type_name = ''
    if int(sort) == 3:
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    elif int(sort) == 2:
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    else:
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    p = Paginator(goods_list, 10)
    page_data = p.page(int(page_num))
    page_num = p.count
    recommand = GoodsInfo.objects.filter(gtype_id=tid).order_by('-id')[0:2]
    context= {'data': page_data, 'page_num': page_num, 'recommand': recommand, 'sort': sort, 'type_name': type_name}
    return render(request, 'goods/list.html', context)


