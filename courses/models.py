#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

from profiles.models import *
from Edu123Kid.views import send_sms

class Course(models.Model):
    COURSE_STATE_CHOICES = [
    (0, u'进行中'),
    (1, u'已完成'),
    ]
    title = models.CharField(blank=True,null=True,max_length=128)
    student = models.ForeignKey(StudentProfile, related_name='course_student')
    start_datetime = models.DateTimeField()
    category = models.CharField(blank=True,null=True,max_length=128)
    state = models.IntegerField(verbose_name='状态',choices=COURSE_STATE_CHOICES,default=0)
    time_span = models.IntegerField(verbose_name='时间间隔',default=7)
    
    class META:
        ordering = ['state']

    def __unicode__(self):
        return self.title

class Class(models.Model):
    CLASS_STATE_CHOICES = [
                     (0, u'未完成'),
                     (1, u'已完成'),
                     ]
    title = models.CharField(blank=True,null=True,max_length=128)
    student = models.ForeignKey(StudentProfile, related_name='class_student')
    mentor = models.ForeignKey(MentorProfile, related_name='class_mentor')
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    state = models.IntegerField(verbose_name='状态',choices=CLASS_STATE_CHOICES,default=0)
                     
    class META:
        ordering = ['state']

    def __unicode__(self):
        return self.title
