# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('writings', '0004_auto_20171228_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='WritingLesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.IntegerField(default=0, null=True, verbose_name='\u72b6\u6001', blank=True, choices=[(0, '\u672a\u4ed8\u6b3e'), (1, '\u672a\u5206\u914d'), (2, '\u6388\u8bfe\u4e2d'), (3, '\u5df2\u7ed3\u8bfe')])),
                ('student', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
