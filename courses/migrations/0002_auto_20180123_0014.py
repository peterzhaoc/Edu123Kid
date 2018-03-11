# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='mentor',
            field=models.ForeignKey(related_name='class_mentor', blank=True, to='profiles.MentorProfile', null=True),
        ),
    ]
