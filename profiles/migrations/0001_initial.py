# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(default='', max_length=16, blank=True)),
                ('sex', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('balance', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=0, verbose_name='\u7528\u6237\u7c7b\u578b', choices=[(0, '\u5b66\u751f'), (1, '\u5bfc\u5e08')])),
            ],
        ),
        migrations.CreateModel(
            name='MentorProfile',
            fields=[
                ('usertype_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='profiles.UserType')),
                ('permission', models.IntegerField(default=0, verbose_name='\u5bfc\u5e08\u6743\u9650', choices=[(0, '\u666e\u901a\u6743\u9650'), (1, '\u9ad8\u7ea7\u6743\u9650'), (2, '\u8d85\u7ea7\u6743\u9650')])),
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
        migrations.AddField(
            model_name='userprofile',
            name='usertype',
            field=models.OneToOneField(null=True, to='profiles.UserType'),
        ),
    ]
