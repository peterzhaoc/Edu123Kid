# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writingtask',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='writingtask',
            name='category',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='writingtask',
            name='publish_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='writingtask',
            name='title',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='writingtask',
            name='writingfile',
            field=models.FileField(null=True, upload_to='static/file', blank=True),
        ),
    ]
