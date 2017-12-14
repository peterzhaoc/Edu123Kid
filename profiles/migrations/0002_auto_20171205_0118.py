# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorprofile',
            name='adept',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='resume',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(default='', max_length=16, null=True, blank=True),
        ),
    ]
