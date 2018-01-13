# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20171226_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.IntegerField(default=0, verbose_name='\u7528\u6237\u7c7b\u578b', choices=[(0, '\u5b66\u751f'), (1, '\u5bfc\u5e08')]),
        ),
    ]
