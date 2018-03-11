# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20180123_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, null=True, blank=True)),
                ('category', models.CharField(max_length=128, null=True, blank=True)),
                ('time_span', models.IntegerField(default=2, verbose_name='\u65f6\u95f4\u95f4\u9694')),
                ('class_count', models.IntegerField(default=4, verbose_name='\u4e0a\u8bfe\u6b21\u6570')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.RemoveField(
            model_name='course',
            name='class_count',
        ),
        migrations.RemoveField(
            model_name='course',
            name='time_span',
        ),
        migrations.RemoveField(
            model_name='course',
            name='title',
        ),
    ]
