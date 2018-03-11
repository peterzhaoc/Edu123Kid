# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20180206_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursebase',
            name='price',
            field=models.IntegerField(default=1000, verbose_name='\u4ef7\u683c'),
        ),
    ]
