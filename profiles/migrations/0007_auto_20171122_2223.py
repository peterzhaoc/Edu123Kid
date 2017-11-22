# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_mentorprofile_studentprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='permission',
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='permission',
            field=models.IntegerField(default=0, verbose_name='\u5bfc\u5e08\u6743\u9650', choices=[(0, '\u666e\u901a\u6743\u9650'), (1, '\u9ad8\u7ea7\u6743\u9650'), (2, '\u8d85\u7ea7\u6743\u9650')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='balance',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=2),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bonus',
            field=models.IntegerField(default=0),
        ),
    ]
