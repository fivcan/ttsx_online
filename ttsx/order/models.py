from django.db import models
from user_center.models import *
from goods.models import *


class OrderInfo(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    user = models.ForeignKey(UserInfo)
    time = models.DateTimeField()
    total = models.DecimalField(max_digits=6, decimal_places=2)
    address = models.CharField(max_length=100)


class OrderDetail(models.Model):
    good = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    xiaoji = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.ForeignKey(OrderInfo)
