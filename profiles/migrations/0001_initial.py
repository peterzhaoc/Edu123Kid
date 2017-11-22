# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(default='', max_length=16, blank=True)),
                ('sex', models.IntegerField(default=0)),
                ('phone', models.CharField(default='', max_length=16, blank=True)),
                ('permission', models.IntegerField(default=0, verbose_name='\u6743\u9650', choices=[(0, '\u666e\u901a\u7528\u6237'), (1, '\u666e\u901a\u5bfc\u5e08'), (2, '\u6838\u5fc3\u5bfc\u5e08'), (3, '\u7ec8\u5ba1\u5bfc\u5e08'), (4, '\u7ba1\u7406\u5458')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
