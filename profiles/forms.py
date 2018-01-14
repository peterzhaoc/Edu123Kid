# -*- coding:utf-8 -*-  
from django import forms
from django.forms import ModelForm
from .models import *

#表单
'''
class UserForm1(forms.Form):
    username = forms.CharField(label='手机号',max_length=13)
    captcha = CaptchaField(label='验证码')
    code = forms.CharField(label='手机号',max_length=6)
'''
class UserForm2(forms.Form):
    password_1 = forms.CharField(label='密码',widget=forms.PasswordInput())
    password_2 = forms.CharField(label='重复密码',widget=forms.PasswordInput())

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
        labels = {
            
            
        }

class StudentProfileForm(ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ['userprofile']
        labels = {
        
        }

class MentorProfileForm(ModelForm):    
    class Meta:
        model = MentorProfile
        exclude = ['userprofile']
        labels = {
        
        }
