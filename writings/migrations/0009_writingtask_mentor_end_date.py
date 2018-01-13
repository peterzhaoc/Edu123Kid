# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0008_auto_20180111_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='writingtask',
            name='mentor_end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 12, 6, 36, 2, 212458, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
