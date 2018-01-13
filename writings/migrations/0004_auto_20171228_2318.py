# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20171226_1754'),
        ('writings', '0003_auto_20171226_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='writingtask',
            old_name='writingfile',
            new_name='originalfile',
        ),
        migrations.AddField(
            model_name='writingtask',
            name='editedfile',
            field=models.FileField(null=True, upload_to='static/file', blank=True),
        ),
        migrations.AddField(
            model_name='writingtask',
            name='finaleditor',
            field=models.ForeignKey(related_name='finaleditor', to='profiles.MentorProfile', null=True),
        ),
        migrations.AddField(
            model_name='writingtask',
            name='finalfile',
            field=models.FileField(null=True, upload_to='static/file', blank=True),
        ),
    ]
