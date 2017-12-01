# -*- coding:utf-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

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
    writingfile = models.FileField(blank=True,null=True,upload_to='static/file')
    author = models.ForeignKey(User)
    publish_date = models.DateField(blank=True,null=True,)
    category = models.CharField(blank=True,null=True,max_length=128)
    state = models.IntegerField(blank=True,null=True,verbose_name='状态',choices=STATE_CHOICES,default=0)    

    class META:
        ordering = ['state']

    def __unicode__(self):
        return self.title

class Img(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    img = models.ImageField(upload_to='image/%Y/%m/%d/')
    book = models.ForeignKey(Book)

    class META:
        ordering = ['name']

    def __unicode__(self):
        return self.name
