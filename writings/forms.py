# -*- coding:utf-
from django import forms

#表单
class WritingTaskForm(forms.Form):
    title = forms.CharField(max_length=128)
    writingfile = forms.FileField()

