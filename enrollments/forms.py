# -*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import *

#表单

class sjmdbmxxForm(ModelForm):
    class Meta:
        model = sjmdbmxx
        exclude = {}
        labels = {}
