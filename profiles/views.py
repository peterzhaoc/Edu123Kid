# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from writings.models import *
from django.core.urlresolvers import reverse
from profiles.utils import permission_check
from .models import *
from .forms import *
import time
import threading
import random
import json
import os
import sys
import uuid
from Edu123Kid.views import send_sms

def index(request):
    user = request.user if request.user.is_authenticated() else None
    content = {
        'user': user,
    }
    return render(request, 'profiles/index.html', content)

'''
# 未使用
def session_delete(request):
    print "delete started"
    time.sleep(3)
    del request.session["verification_code"]
    print "delete success"
    return
'''

# 生成六位随机数
def generate_verification_code():
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))
    
    myslice = random.sample(code_list, 6)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice) # list to string
    return verification_code

def get_verification_code(request):
    if request.method == 'POST':
        verification_code = generate_verification_code()
        params = "{\"code\":\"" + verification_code + "\",\"product\":\"云通信\"}"
        #print send_sms(request.POST['phone_number'], "越读悦写", "SMS_112465062", params)
        print verification_code
        request.session["verification_code"] = verification_code
        request.session.set_expiry(300)
        #t = threading.Thread(target=session_delete, args=(request,))
        #t.start()
    html = ""
    return HttpResponse(html)

def signup(request):
    state = ""
    user = request.user if request.user.is_authenticated() else None
    if user:
        return HttpResponseRedirect(reverse('user_profile'))
    elif request.method == 'POST':
        if request.POST["verification_code"] == request.session.get("verification_code", default=None):
            request.session["phone_number"] = request.POST["phone_number"]
            return HttpResponseRedirect(reverse('set_password'))
        else:
            content = {
            'state': "verification_code_not_match",
            'user': None
            }
            return render(request, 'profiles/signup.html', content)
    else:
        content = {
            'state': state,
            'user': None
        }
        return render(request, 'profiles/signup.html')

def set_password(request):
    state = None
    if request.method == 'POST':
        phone_number = request.session.get("phone_number", default=None)
        new_password = request.POST.get('new_password', '')
        nickname = request.POST.get('nickname', phone_number)
        repeat_password = request.POST.get('repeat_password', '')
        option = request.POST.get('inlineRadioOptions', '')
        if not new_password:
            state = 'empty'
        elif new_password != repeat_password:
            state = 'repeat_error'
        else:
            new_user = User.objects.create_user(username=phone_number, password=new_password)
            new_user.save()
            del request.session["phone_number"]
            userlogin = auth.authenticate(username=phone_number, password=new_password)
            auth.login(request, userlogin)
            profile = UserProfile()
            profile.user = new_user
            profile.nickname = nickname
            profile.save()

            if option == 'option1':
                usertype = StudentProfile(userprofile=profile,)
                profile.type = 0
            elif option == 'option2':
                usertype = MentorProfile(userprofile=profile,)
                profile.type = 1
            usertype.save()
            profile.save()
            request.session.set_expiry(1800)
            return HttpResponseRedirect(reverse('homepage'))
        content ={'user': None,'state': state,}
        return render(request, 'profiles/set_password.html', content)
    else:
        content ={'user': None,'state': state,}
        return render(request, 'profiles/set_password.html', content)

def signup2(request):
    user = request.user if request.user.is_authenticated() else None
    if user:
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    form = UserForm1()
    if request.method == 'POST':
        form = UserForm1(request.POST)
        password = form.password_1
        repeat_password = form.password_2
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create_user(username=username, password=password,
                                                    email=request.POST.get('email', ''))
                new_user.save()
                new_my_user = MyUser(user=new_user, nickname=request.POST.get('nickname', ''))
                new_my_user.save()
                state = 'success'
    content = {
        'form':form,
        'state': state,
        'user': None,
    }
    return render(request, 'profiles/signup.html', content)


def login(request):
    user = request.user if request.user.is_authenticated() else None
    if user:
        return HttpResponseRedirect(reverse('user_profile'))
    elif request.method == 'GET':
        state = request.GET.get('state', '')
        content = {
                  'state': state,
                  'user': None
                  }
        return render(request, 'profiles/login.html', content)
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            state = 'success'
        else:
            state = 'not_exist_or_password_error'
        return HttpResponse(state)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))


@login_required
def set_password2(request):
    user = request.user if request.user.is_authenticated() else None
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'
        else:
            state = 'password_error'
    content = {
        'user': user,
        'active_menu': 'homepage',
        'state': state,
    }
    return render(request, 'management/set_password.html', content)

@login_required
def user_profile(request):
    user = request.user if request.user.is_authenticated() else None
    profile = user.userprofile
    type = profile.type
    studentform = StudentProfileForm()
    mentorform = MentorProfileForm()
    profileform = UserProfileForm(instance=profile)
    if type == 0:
        studentform = StudentProfileForm(instance=StudentProfile.objects.get(userprofile=profile))
    else:
        mentorform = MentorProfileForm(instance=MentorProfile.objects.get(userprofile=profile))

    content = {
        'type': type,
        'profileform': profileform,
        'studentform': studentform,
        'mentorform': mentorform,
        'user': user,
        'profile': profile,
    }
    return render(request, 'profiles/user_profile.html', content)
