#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

from profiles.models import *
from Edu123Kid.views import send_sms

class Book(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    author = models.CharField(max_length=128)
    publish_date = models.DateField()
    category = models.CharField(max_length=128)

    class META:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class WritingTask(models.Model):
    STATE_CHOICES = [
    (0, u'未付款'),
    (1, u'未审核'),
    (2, u'批改中'),
    (3, u'终审中'),
    (4, u'已完成'),
    ]
    title = models.CharField(blank=True,null=True,max_length=128)
    originalfile = models.FileField(blank=True,null=True,upload_to='static/file')
    author = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(verbose_name='上传时间')
    mentor_end_date = models.DateTimeField(verbose_name='导师截止时间')
    end_date = models.DateTimeField(verbose_name='终审截止时间')
    category = models.CharField(blank=True,null=True,max_length=128)
    state = models.IntegerField(blank=True,null=True,verbose_name='状态',choices=STATE_CHOICES,default=0)
    pay = models.IntegerField(default=30,verbose_name='工资')
    editor = models.ForeignKey(MentorProfile,blank=True,null=True,related_name='editor')
    editedfile = models.FileField(blank=True,null=True,upload_to='static/file')
    finaleditor = models.ForeignKey(MentorProfile,blank=True,null=True,related_name='finaleditor')
    finalfile = models.FileField(blank=True,null=True,upload_to='static/file')
    

    class META:
        ordering = ['state']

    def __unicode__(self):
        return self.title

    def distribute(self):
        mentor_list = MentorProfile.objects.filter(isvalid=True, permission=1)
        if mentor_list.count() > 0:
            mentor = mentor_list[0]
            self.editor = mentor
            self.save()
            mentor.isvalid = False
            mentor.save()
            phonenumber = mentor.userprofile.user.username
            params = "{\"expiredate\":\"" + self.mentor_end_date.strftime('%Y-%m-%d') + "\",\"product\":\"云通信\"}"
            #print repr(params)
            print send_sms(phonenumber, u'越读悦写'.encode("utf8"), "SMS_120130649", params.encode("utf8"))
            self.state = 2
            return True
        else:
            return False

    def final_distribute(self):
        mentor_list = MentorProfile.objects.filter(isvalid=True, permission=3)
        self.state = 3
        if mentor_list.count() > 0:
            mentor = mentor_list[0]
            self.finaleditor = mentor
            self.save()
            phonenumber = mentor.userprofile.user.username
            params = "{\"expiredate\":\"" + self.end_date.strftime('%Y-%m-%d') + "\",\"product\":\"云通信\"}"
            #print repr(params)
            print send_sms(phonenumber, u'越读悦写'.encode("utf8"), "SMS_121855941", params.encode("utf8"))
            return True
        else:
            return False

    def expire_remind(self):
        mentor = self.editor
        if mentor:
            phonenumber = self.editor.userprofile.user.username
            print phonenumber + phonenumber + phonenumber
            try:
                params = "{\"title\":\"" + self.title + "\",\"product\":\"云通信\"}"
                print send_sms(phonenumber, u'越读悦写'.encode("utf8"), "SMS_120120626", params.encode("utf8"))
                return True
            except:
                return False
        else:
            return False

class Img(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    img = models.ImageField(upload_to='image/%Y/%m/%d/')
    book = models.ForeignKey(Book)

    class META:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class WritingLesson(models.Model):
    STATE_CHOICES = [
                     (0, u'未付款'),
                     (1, u'未分配'),
                     (2, u'授课中'),
                     (3, u'已结课'),
                     ]
    student = models.ForeignKey(User)
    state = models.IntegerField(blank=True,null=True,verbose_name='状态',choices=STATE_CHOICES,default=0)
        
    class META:
        ordering = ['state']

    def __unicode__(self):
        return self.title
