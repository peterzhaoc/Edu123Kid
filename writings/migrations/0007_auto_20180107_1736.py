# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0006_auto_20180101_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writingtask',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='writingtask',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
