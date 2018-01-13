# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0007_auto_20180107_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writingtask',
            name='editor',
            field=models.ForeignKey(related_name='editor', blank=True, to='profiles.MentorProfile', null=True),
        ),
        migrations.AlterField(
            model_name='writingtask',
            name='finaleditor',
            field=models.ForeignKey(related_name='finaleditor', blank=True, to='profiles.MentorProfile', null=True),
        ),
    ]
