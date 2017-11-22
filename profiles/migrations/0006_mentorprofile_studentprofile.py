# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_userprofile_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorProfile',
            fields=[
                ('usertype_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='profiles.UserType')),
                ('prefer', models.IntegerField(default=2, verbose_name='\u503e\u5411', choices=[(0, '\u5c0f\u5b66\u4f5c\u6587'), (1, '\u521d\u4e2d\u4f5c\u6587'), (2, '\u7686\u53ef')])),
                ('adept', models.TextField()),
                ('resume', models.TextField()),
            ],
            bases=('profiles.usertype',),
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('usertype_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='profiles.UserType')),
                ('grade', models.PositiveIntegerField(default=1, verbose_name='\u5e74\u7ea7', choices=[(1, '\u4e00\u5e74\u7ea7'), (2, '\u4e8c\u5e74\u7ea7'), (3, '\u4e09\u5e74\u7ea7'), (4, '\u56db\u5e74\u7ea7'), (5, '\u4e94\u5e74\u7ea7'), (6, '\u516d\u5e74\u7ea7'), (7, '\u4e03\u5e74\u7ea7'), (8, '\u516b\u5e74\u7ea7'), (9, '\u4e5d\u5e74\u7ea7')])),
            ],
            bases=('profiles.usertype',),
        ),
    ]
