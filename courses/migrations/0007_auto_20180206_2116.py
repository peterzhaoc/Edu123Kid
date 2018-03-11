# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_course_course_base'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_base',
            field=models.ForeignKey(related_name='course_base', to='courses.CourseBase'),
        ),
    ]
