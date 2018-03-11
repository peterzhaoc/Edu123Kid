# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20180206_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_base',
            field=models.ForeignKey(related_name='course_base', to='courses.CourseBase', null=True),
        ),
    ]
