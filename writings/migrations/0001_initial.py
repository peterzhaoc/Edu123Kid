# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('price', models.FloatField()),
                ('author', models.CharField(max_length=128)),
                ('publish_date', models.DateField()),
                ('category', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='image/%Y/%m/%d/')),
                ('book', models.ForeignKey(to='writings.Book')),
            ],
        ),
        migrations.CreateModel(
            name='WritingLesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.IntegerField(default=0, null=True, verbose_name='\u72b6\u6001', blank=True, choices=[(0, '\u672a\u4ed8\u6b3e'), (1, '\u672a\u5206\u914d'), (2, '\u6388\u8bfe\u4e2d'), (3, '\u5df2\u7ed3\u8bfe')])),
                ('student', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WritingTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, null=True, blank=True)),
                ('originalfile', models.FileField(null=True, upload_to='static/file', blank=True)),
                ('publish_date', models.DateTimeField()),
                ('mentor_end_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('category', models.CharField(max_length=128, null=True, blank=True)),
                ('state', models.IntegerField(default=0, null=True, verbose_name='\u72b6\u6001', blank=True, choices=[(0, '\u672a\u4ed8\u6b3e'), (1, '\u672a\u5ba1\u6838'), (2, '\u6279\u6539\u4e2d'), (3, '\u7ec8\u5ba1\u4e2d'), (4, '\u5df2\u5b8c\u6210')])),
                ('editedfile', models.FileField(null=True, upload_to='static/file', blank=True)),
                ('finalfile', models.FileField(null=True, upload_to='static/file', blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('editor', models.ForeignKey(related_name='editor', blank=True, to='profiles.MentorProfile', null=True)),
                ('finaleditor', models.ForeignKey(related_name='finaleditor', blank=True, to='profiles.MentorProfile', null=True)),
            ],
        ),
    ]
