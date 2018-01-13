# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20180101_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorprofile',
            name='isvalid',
            field=models.BooleanField(verbose_name='\u7a7a\u95f2'),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='resume',
            field=models.TextField(null=True, verbose_name='\u7b80\u5386', blank=True),
        ),
    ]
