# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('writings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='writingtask',
            name='editor',
            field=models.ForeignKey(related_name='editor', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='writingtask',
            name='author',
            field=models.ForeignKey(related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
