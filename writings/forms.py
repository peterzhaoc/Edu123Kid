# -*- coding:utf-8 -*-
from django import forms

#表单
class WritingTaskAddForm(forms.Form):
    title = forms.CharField(max_length=30,label=u'作文标题')
    originalfile = forms.FileField(label=u'上传文件')

class WritingTaskEditForm(forms.Form):
    editedfile = forms.FileField(label=u'上传修改文件')
