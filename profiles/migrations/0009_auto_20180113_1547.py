# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20180101_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='classes',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='classes',
            field=models.IntegerField(default=0, verbose_name='\u5269\u4f59\u8bfe\u7a0b\u6570'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(default='\u7528\u6237', max_length=16, null=True, verbose_name='\u6635\u79f0', blank=True),
        ),
    ]
