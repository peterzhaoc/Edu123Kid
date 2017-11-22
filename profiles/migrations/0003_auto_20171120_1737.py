# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_auto_20171120_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(default='', max_length=16, blank=True)),
                ('sex', models.IntegerField(default=0)),
                ('permission', models.IntegerField(default=0, verbose_name='\u7528\u6237\u6743\u9650', choices=[(0, '\u666e\u901a\u6743\u9650'), (1, '\u9ad8\u7ea7\u6743\u9650'), (2, '\u8d85\u7ea7\u6743\u9650')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='mentorprofile',
            old_name='usertype',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='studentprofile',
            old_name='usertype',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='mentorprofile',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='mentorprofile',
            name='permission',
        ),
        migrations.RemoveField(
            model_name='mentorprofile',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='mentorprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='permission',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='user',
        ),
    ]
