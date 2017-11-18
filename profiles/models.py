# -*- coding:utf-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    PERMISSION_CHOICES = [
                          (0, u'普通用户'),
                          (1, u'普通导师'),
                          (2, u'核心导师'),
                          (3, u'终审导师'),
                          (4, u'管理员'),
                          ]
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16, default='', blank=True)
    sex = models.IntegerField(default=0)
    phone = models.CharField(max_length=16, default='', blank=True)
    permission = models.IntegerField(verbose_name='权限',choices=PERMISSION_CHOICES,default=0)
    
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
