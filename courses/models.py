#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

from profiles.models import *
from Edu123Kid.views import send_sms
import datetime

class CourseBase(models.Model):
    title = models.CharField(blank=True,null=True,max_length=128)
    category = models.CharField(blank=True,null=True,max_length=128)
    time_span = models.IntegerField(verbose_name='时间间隔',default=2)
    class_count = models.IntegerField(verbose_name='上课次数',default=4)
    price = models.IntegerField(verbose_name='价格',default=1000)

    def __unicode__(self):
        return self.title

class Course(models.Model):
    COURSE_STATE_CHOICES = [
    (0, u'进行中'),
    (1, u'已完成'),
    ]
    course_base = models.ForeignKey(CourseBase, related_name='course_base')
    student = models.ForeignKey(StudentProfile, related_name='course_student')
    start_datetime = models.DateTimeField()
    state = models.IntegerField(verbose_name='状态',choices=COURSE_STATE_CHOICES,default=0)
    
    class META:
        ordering = ['state']

    def __unicode__(self):
        return self.course_base


    def check_mentor_available(self, mentor):
        time = self.start_datetime
        for i in range(self.course_base.class_count):
            try:  
                Class.objects.get(mentor=mentor, start_datetime=time)
                return False
            except Class.DoesNotExist:
                time = time + datetime.timedelta(days=self.course_base.time_span)
        return True

    def create_classes(self):
        mentors = MentorProfile.objects.filter(permission__gte=2)
        if mentors:
            mentor = None
            for m in mentors:
                if self.check_mentor_available(m):
                    mentor = m
                    break
    
            time = self.start_datetime
            for i in range(self.course_base.class_count):
                new_class = Class(
                              course=self,
                              course_index=i,
                              student=self.student,
                              mentor=mentor,
                              start_datetime=time,
                              end_datetime=time+datetime.timedelta(hours=1),
                             )
                new_class.save()
                time = time + datetime.timedelta(days=self.time_span)
            return True
        else:
            return False

class Class(models.Model):
    CLASS_STATE_CHOICES = [
                     (0, u'未完成'),
                     (1, u'已完成'),
                     ]
    course_index = models.IntegerField(verbose_name='序号')
    course = models.ForeignKey(Course)
    student = models.ForeignKey(StudentProfile, related_name='class_student')
    mentor = models.ForeignKey(MentorProfile, related_name='class_mentor', blank=True, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    state = models.IntegerField(verbose_name='状态',choices=CLASS_STATE_CHOICES,default=0)
                     
    class META:
        ordering = ['state']

    def __unicode__(self):
        return self.course.course_base.title
