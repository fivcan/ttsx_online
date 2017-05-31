from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)
    address = models.CharField(max_length=40, default='')
    receiver = models.CharField(max_length=20, default='')
    postcode = models.CharField(max_length=20, default='')
    tel = models.CharField(max_length='20', default='')

    def __str__(self):
        return self.user