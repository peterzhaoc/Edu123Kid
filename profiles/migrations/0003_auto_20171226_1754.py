# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_mentorprofile_invalid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentorprofile',
            old_name='invalid',
            new_name='isvalid',
        ),
    ]
