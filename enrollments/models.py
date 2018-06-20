#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

from profiles.models import *
from Edu123Kid.views import send_sms

class sjmdbmxx(models.Model):

    name = models.CharField(max_length=20,verbose_name='学生姓名')
    phone = models.IntegerField(verbose_name='家长电话')
    school = models.CharField(max_length=20,verbose_name='学校')
    gclass = models.CharField(max_length=20,verbose_name='班级')
    
    class META:
        ordering = ['school']

    def __unicode__(self):
        return self.name
