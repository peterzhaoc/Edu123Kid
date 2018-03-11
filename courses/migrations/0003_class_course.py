# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180123_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(blank=True, to='courses.Course', null=True),
        ),
    ]
