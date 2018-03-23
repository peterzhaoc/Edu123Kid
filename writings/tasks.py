# -*- coding:utf-8 -*-
from Edu123Kid.celery import app
from celery.schedules import crontab
import datetime
from .models import *
import pytz

@app.task
def writing_task_expire_remind():
    now = datetime.datetime.now().replace(tzinfo=pytz.timezone('UTC'))
    d = datetime.timedelta(2)
    writing_task_list = WritingTask.objects.all()
    for writing_task in writing_task_list:
        end = writing_task.end_date
        timedelta = end - now

        if timedelta < d and end > now:
            writing_task.expire_remind()

app.conf.update(
                CELERYBEAT_SCHEDULE = {
                'check_due_writing_tasks': {
                'task': 'writings.tasks.writing_task_expire_remind',
                'schedule': crontab(hour=23, minute=20),
                },
                }
                )
