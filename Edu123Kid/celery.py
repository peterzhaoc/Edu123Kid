# -*- coding:utf-8 -*-
from __future__ import absolute_import
import os
import django
from celery import Celery,platforms
from django.conf import settings
from django.apps import apps
from datetime import datetime,timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Edu123Kid.settings')
django.setup()
platforms.C_FORCE_ROOT = True
app = Celery('Edu123Kid')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
#app.config_from_object('config')


