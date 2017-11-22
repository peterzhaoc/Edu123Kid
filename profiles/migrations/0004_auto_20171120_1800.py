# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20171120_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=0, verbose_name='\u7528\u6237\u7c7b\u578b', choices=[(0, '\u5b66\u751f'), (1, '\u5bfc\u5e08')])),
            ],
        ),
        migrations.DeleteModel(
            name='MentorProfile',
        ),
        migrations.DeleteModel(
            name='StudentProfile',
        ),
    ]
