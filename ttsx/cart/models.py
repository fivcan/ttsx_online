from django.db import models
from user_center.models import *
from goods.models import *

class CartInfo(models.Model):
    good = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
    user = models.ForeignKey(UserInfo)
