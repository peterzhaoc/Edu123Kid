# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# 用户档案
class UserProfile(models.Model):
    TYPE_CHOICES = [
                    (0, u'学生'),
                    (1, u'导师'),
                    ]
    user = models.OneToOneField(User)
    nickname = models.CharField(verbose_name='昵称', max_length=16, default='用户', blank=True, null=True)
    sex = models.IntegerField(verbose_name='性别', default=0)
    bonus = models.IntegerField(verbose_name='积分', default=0)
    balance = models.DecimalField(verbose_name='余额', max_digits=8,decimal_places=2,default=0)
    type = models.IntegerField(verbose_name='用户类型',choices=TYPE_CHOICES,default=0)
    def __str__(self):
        return self.nickname
    
    def __unicode__(self):
        return self.nickname

'''
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)
'''
class StudentProfile(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
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
    grade = models.PositiveIntegerField(verbose_name='年级',choices=Grade_CHOICES,blank=True,null=True)
    classes = models.IntegerField(verbose_name='剩余课程数', default=0)
    def __str__(self):
        return self.userprofile.nickname
    
    def __unicode__(self):
        return self.userprofile.nickname


class MentorProfile(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    isvalid = models.BooleanField(verbose_name='空闲',default=True)
    Prefer_CHOICES = [
                     (0, u'小学作文'),
                     (1, u'初中作文'),
                     (2, u'皆可'),
                     ]
    PERMISSION_CHOICES = [
                             (0, u'助教'),
                             (1, u'作文批改导师'),
                             (2, u'授课导师'),
                             (3, u'终审导师'),
                         ]
    permission = models.IntegerField(verbose_name='导师权限',choices=PERMISSION_CHOICES,default=0)
    prefer = models.IntegerField(verbose_name='倾向',choices=Prefer_CHOICES,default=2)
    adept = models.TextField(verbose_name='擅长',blank=True, null=True)
    resume = models.TextField(verbose_name='简历', blank=True, null=True)

    def __str__(self):
        return self.userprofile.nickname
    
    def __unicode__(self):
        return self.userprofile.nickname
