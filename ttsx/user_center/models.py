from django.db import models

# Create your models here.

class Users(models.Model):
    user = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)
    address = models.CharField(max_length=40, default='')
    receiver = models.CharField(max_length=20, default='')
    postcod = models.IntegerField(default='')
    tel = models.CharField(max_length='20',default='')
