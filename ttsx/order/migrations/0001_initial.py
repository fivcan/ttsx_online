# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('xiaoji', models.DecimalField(max_digits=6, decimal_places=2)),
                ('good', models.ForeignKey(to='goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('time', models.DateTimeField()),
                ('total', models.DecimalField(max_digits=6, decimal_places=2)),
                ('address', models.CharField(max_length=100)),
                ('user', models.ForeignKey(to='user_center.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(to='order.OrderInfo'),
        ),
    ]
