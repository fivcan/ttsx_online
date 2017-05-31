# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=50)),
                ('address', models.CharField(default=b'', max_length=40)),
                ('receiver', models.CharField(default=b'', max_length=20)),
                ('postcode', models.CharField(default=b'', max_length=20)),
                ('tel', models.CharField(default=b'', max_length=b'20')),
            ],
        ),
    ]
