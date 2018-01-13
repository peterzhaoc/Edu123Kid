# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0005_writinglesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='writingtask',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2018, 1, 1, 14, 44, 54, 388517, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='writingtask',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2018, 1, 1, 14, 45, 18, 893717, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
