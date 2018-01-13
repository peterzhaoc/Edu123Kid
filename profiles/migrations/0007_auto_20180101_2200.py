# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20180101_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='classes',
            field=models.IntegerField(default=0, verbose_name='\u5269\u4f59\u8bfe\u7a0b\u6570'),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='adept',
            field=models.TextField(null=True, verbose_name='\u64c5\u957f', blank=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='isvalid',
            field=models.BooleanField(default=True, verbose_name='\u7a7a\u95f2'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.DecimalField(default=0, verbose_name='\u4f59\u989d', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bonus',
            field=models.IntegerField(default=0, verbose_name='\u79ef\u5206'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(default='', max_length=16, null=True, verbose_name='\u6635\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.IntegerField(default=0, verbose_name='\u6027\u522b'),
        ),
    ]
