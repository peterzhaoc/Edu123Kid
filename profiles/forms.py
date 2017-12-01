# -*- coding:utf-
from django import forms
from captcha.fields import CaptchaField
#表单
class UserForm1(forms.Form):
    username = forms.CharField(label='手机号',max_length=13)
    captcha = CaptchaField(label='验证码')
    code = forms.CharField(label='手机号',max_length=6)

class UserForm2(forms.Form):
    password_1 = forms.CharField(label='密码',widget=forms.PasswordInput())
    password_2 = forms.CharField(label='重复密码',widget=forms.PasswordInput())
