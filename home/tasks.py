# -*- coding:utf-8 -*-
from Edu123Kid.celery import app
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from celery.schedules import crontab
from datetime import datetime, timedelta

@app.task
def hello_world():
    print('Hello World,fvf')

@app.task
def sendEmail():
    fromaddr = "peterzhaoc@126.com"
    toaddr = "peterzhaoc@126.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SUBJECT OF THE MAIL"
    
    body = "YOUR MESSAGE HERE"
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.126.com',25)
    server.starttls()
    server.login(fromaddr, "peter12808891")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return
'''
app.conf.update(
                CELERYBEAT_SCHEDULE = {
                'check_due_writing_tasks': {
                'task': 'home.tasks.sendEmail',
                'schedule': timedelta(seconds=15),
                },
                }
                )
'''
