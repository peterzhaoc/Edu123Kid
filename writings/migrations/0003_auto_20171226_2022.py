# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0002_auto_20171226_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writingtask',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='writingtask',
            name='editor',
            field=models.ForeignKey(related_name='editor', to='profiles.MentorProfile', null=True),
        ),
    ]
