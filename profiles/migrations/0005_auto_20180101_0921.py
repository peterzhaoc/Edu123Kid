# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20171230_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorprofile',
            name='userprofile',
            field=models.ForeignKey(to='profiles.UserProfile'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='userprofile',
            field=models.ForeignKey(to='profiles.UserProfile'),
        ),
    ]
