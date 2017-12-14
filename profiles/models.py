# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserType(models.Model):
    TYPE_CHOICES = [
                    (0, u'学生'),
                    (1, u'导师'),
                    ]
    type = models.IntegerField(verbose_name='用户类型',choices=TYPE_CHOICES,default=0)
    
    def __str__(self):
        return self.type
    
    def __unicode__(self):
        return self.type

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    usertype = models.OneToOneField(UserType, null=True)
    nickname = models.CharField(max_length=16, default='', blank=True, null=True)
    sex = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    balance = models.DecimalField(max_digits=8,decimal_places=2,default=0)
    
    def __str__(self):
        return self.nickname
    
    def __unicode__(self):
        return self.nickname

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)



class StudentProfile(UserType):
    Grade_CHOICES = [
                    (1, u'一年级'),
                    (2, u'二年级'),
                    (3, u'三年级'),
                    (4, u'四年级'),
                    (5, u'五年级'),
                    (6, u'六年级'),
                    (7, u'七年级'),
                    (8, u'八年级'),
                    (9, u'九年级'),
                    ]
    grade = models.PositiveIntegerField(verbose_name='年级',choices=Grade_CHOICES,default=1)

class MentorProfile(UserType):
    Prefer_CHOICES = [
                     (0, u'小学作文'),
                     (1, u'初中作文'),
                     (2, u'皆可'),
                     ]
    PERMISSION_CHOICES = [
                         (0, u'普通权限'),
                         (1, u'高级权限'),
                         (2, u'超级权限'),
                         ]
    permission = models.IntegerField(verbose_name='导师权限',choices=PERMISSION_CHOICES,default=0)
    prefer = models.IntegerField(verbose_name='倾向',choices=Prefer_CHOICES,default=2)
    adept = models.TextField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
