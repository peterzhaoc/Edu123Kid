# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from enrollments.models import *
from django.core.urlresolvers import reverse
from profiles.utils import permission_check, mentor_permission_check, student_permission_check
import datetime
import json

def sjmdbmym(request):
    form = sjmdbmxxForm()
    if request.method == 'POST':
        form = sjmdbmxxForm(request.POST)
        if form.is_valid():
            form.save()
    content = {
        'form':form,
    }
    return render(request, 'sjmdbmym.html', content)

