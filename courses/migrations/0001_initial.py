# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_index', models.IntegerField(verbose_name='\u5e8f\u53f7')),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('state', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u672a\u5b8c\u6210'), (1, '\u5df2\u5b8c\u6210')])),
                ('mentor', models.ForeignKey(related_name='class_mentor', to='profiles.MentorProfile')),
                ('student', models.ForeignKey(related_name='class_student', to='profiles.StudentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, null=True, blank=True)),
                ('start_datetime', models.DateTimeField()),
                ('category', models.CharField(max_length=128, null=True, blank=True)),
                ('state', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u8fdb\u884c\u4e2d'), (1, '\u5df2\u5b8c\u6210')])),
                ('time_span', models.IntegerField(default=2, verbose_name='\u65f6\u95f4\u95f4\u9694')),
                ('class_count', models.IntegerField(default=4, verbose_name='\u4e0a\u8bfe\u6b21\u6570')),
                ('student', models.ForeignKey(related_name='course_student', to='profiles.StudentProfile')),
            ],
        ),
    ]
