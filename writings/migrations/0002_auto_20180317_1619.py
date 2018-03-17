# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writingtask',
            name='author',
            field=models.ForeignKey(to='profiles.StudentProfile'),
        ),
        migrations.AlterField(
            model_name='writingtask',
            name='end_date',
            field=models.DateTimeField(verbose_name='\u7ec8\u5ba1\u622a\u6b62\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='writingtask',
            name='mentor_end_date',
            field=models.DateTimeField(verbose_name='\u5bfc\u5e08\u622a\u6b62\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='writingtask',
            name='publish_date',
            field=models.DateTimeField(verbose_name='\u4e0a\u4f20\u65f6\u95f4'),
        ),
    ]
