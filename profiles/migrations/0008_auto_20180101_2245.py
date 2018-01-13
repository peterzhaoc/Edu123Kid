# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20180101_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorprofile',
            name='permission',
            field=models.IntegerField(default=0, verbose_name='\u5bfc\u5e08\u6743\u9650', choices=[(0, '\u52a9\u6559'), (1, '\u4f5c\u6587\u6279\u6539\u5bfc\u5e08'), (2, '\u6388\u8bfe\u5bfc\u5e08'), (3, '\u7ec8\u5ba1\u5bfc\u5e08')]),
        ),
    ]
