# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from writings.models import *
from profiles.models import *
from writings.forms import *
from django.core.urlresolvers import reverse
from profiles.utils import permission_check, mentor_permission_check, student_permission_check
import datetime
import json
from Edu123Kid.views import send_sms

@user_passes_test(permission_check)
def add_book(request):
    user = request.user
    state = None
    if request.method == 'POST':
        new_book = Book(
                name=request.POST.get('name', ''),
                author=request.POST.get('author', ''),
                category=request.POST.get('category', ''),
                price=request.POST.get('price', 0),
                publish_date=request.POST.get('publish_date', '')
        )
        new_book.save()
        state = 'success'
    content = {
        'user': user,
        'active_menu': 'add_book',
        'state': state,
    }
    return render(request, 'management/add_book.html', content)

def view_book_list(request):
    user = request.user if request.user.is_authenticated() else None
    category_list = Book.objects.values_list('category', flat=True).distinct()
    query_category = request.GET.get('category', 'all')
    if (not query_category) or Book.objects.filter(category=query_category).count() is 0:
        query_category = 'all'
        book_list = Book.objects.all()
    else:
        book_list = Book.objects.filter(category=query_category)

    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        book_list = Book.objects.filter(name__contains=keyword)
        query_category = 'all'

    paginator = Paginator(book_list, 5)
    page = request.GET.get('page')
    try:
        book_list = paginator.page(page)
    except PageNotAnInteger:
        book_list = paginator.page(1)
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)
    content = {
        'user': user,
        'active_menu': 'view_book',
        'category_list': category_list,
        'query_category': query_category,
        'book_list': book_list,
    }
    return render(request, 'management/view_book_list.html', content)


def writing_task_detail(request,d):
    user = request.user if request.user.is_authenticated() else None
    profile = user.userprofile
    type = profile.type
    writing_task_id = d
    
    if writing_task_id == '':
        return HttpResponseRedirect(reverse('view_writing_task_list'))
    writing_task = WritingTask.objects.get(id=d)

    upload = False
    if type == 0:
        mentorprofile = None
    else:
        mentorprofile = MentorProfile.objects.get(userprofile=profile)
        if writing_task.state == 2 and writing_task.editor == mentorprofile:
            upload = True
        elif writing_task.state == 3 and writing_task.finaleditor == mentorprofile:
            upload = True

    if request.method == 'POST':
        if writing_task.state == 2:
            writing_task.editedfile = request.FILES.get('chosen_file',None)
            writing_task.final_distribute()
            writing_task.save()
            return HttpResponseRedirect(reverse('my_writing_tasks'))
        elif writing_task.state == 3:
            writing_task.editedfile = request.FILES.get('chosen_file',None)
            writing_task.state = 4
            writing_task.save()
            return HttpResponseRedirect(reverse('my_writing_tasks'))

    content = {
        'upload': upload,
        'type': type,
        'user': user,
        'writing_task': writing_task,
        'mentorprofile': mentorprofile,
    }
    return render(request, 'writings/detail.html', content)


@user_passes_test(permission_check)
def add_img(request):
    user = request.user
    state = None
    if request.method == 'POST':
        try:
            new_img = Img(
                    name=request.POST.get('name', ''),
                    description=request.POST.get('description', ''),
                    img=request.FILES.get('img', ''),
                    book=Book.objects.get(pk=request.POST.get('book', ''))
            )
            new_img.save()
        except Book.DoesNotExist as e:
            state = 'error'
            print(e)
        else:
            state = 'success'
    content = {
        'user': user,
        'state': state,
        'book_list': Book.objects.all(),
        'active_menu': 'add_img',
    }
    return render(request, 'management/add_img.html', content)

@user_passes_test(student_permission_check)
def add_writing_task(request):
    user = request.user if request.user.is_authenticated() else None
    studentprofile = StudentProfile.objects.get(userprofile=user.userprofile)
    if request.method == 'POST':
        form = WritingTaskAddForm(request.POST,request.FILES)
        if form.is_valid():
            new_writing_task = WritingTask(
                title=form.cleaned_data['title'],
                originalfile=form.cleaned_data['originalfile'],
                author=user,
                publish_date=datetime.datetime.now(),
                mentor_end_date=datetime.datetime.now() + datetime.timedelta(days=4),
                end_date=datetime.datetime.now() + datetime.timedelta(days=5),
            )
            if studentprofile.classes > 0:
                studentprofile.classes -= 1
                studentprofile.save()
                new_writing_task.state = 1
                new_writing_task.distribute()

            new_writing_task.save()
        return HttpResponseRedirect("/writings/mywritingtasks/")
    else:
        form = WritingTaskAddForm()

    content = {
        'user': user,
        'form': form,
    }
    return render(request, 'writings/add_writing_task.html', content)

@user_passes_test(permission_check)
def distribute_writing_task(request, d):
    user = request.user
    __business_id = uuid.uuid1()
#if request.method == 'POST':
    writing_task = WritingTask.objects.get(id=d)
    writing_task.save()
    writing_task.distribute()
    return HttpResponseRedirect("/writings/view_writing_task/detail/?id=" + d)
    
#return render(request, '404.html', content)

@user_passes_test(mentor_permission_check)
def view_writing_task_list(request):
    user = request.user if request.user.is_authenticated() else None
    writing_task_list = WritingTask.objects.filter(state=1)
    
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        writing_task_list = WritingTask.objects.filter(title__contains=keyword,state=1)
    
    paginator = Paginator(writing_task_list, 10)
    page = request.GET.get('page')
    try:
        writing_task_list = paginator.page(page)
    except PageNotAnInteger:
        writing_task_list = paginator.page(1)
    except EmptyPage:
        writing_task_list = paginator.page(paginator.num_pages)

    for writing_task in writing_task_list:
        writing_task.finished = 1

    content = {
        'user': user,
        'writing_task_list': writing_task_list,
    }
    return render(request, 'writings/view_writing_list.html', content)


@login_required
def my_writing_tasks(request):
    user = request.user if request.user.is_authenticated() else None
    profile = user.userprofile
    type = profile.type
    
    # get query state
    choices = WritingTask.STATE_CHOICES
    state_list = []
    for i in choices:
        state_list.append(i[1])
    
    query_state_readable = request.GET.get('state', 'all')
    if query_state_readable == 'all':
        query_state = 'all'
    else:
        for j in choices:
            if (query_state_readable == j[1]):
                query_state = j[0]
                break

    if type == 0:
        if (query_state == 'all'):
            writing_task_list = WritingTask.objects.filter(author=user)
        else:
            writing_task_list = WritingTask.objects.filter(author=user).filter(state=query_state)
    else:
        mentorprofile = MentorProfile.objects.get(userprofile=profile)
        if (query_state == 'all'):
            writing_task_list = WritingTask.objects.filter(Q(editor=mentorprofile) | Q(finaleditor=mentorprofile))
        else:
            writing_task_list = WritingTask.objects.filter(Q(editor=mentorprofile) | Q(finaleditor=mentorprofile)).filter(state=query_state)

    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        writing_task_list = WritingTask.objects.filter(Q(editor=mentorprofile,title__contains=keyword) | Q(finaleditor=mentorprofile,title__contains=keyword))
        query_state = 'all'
    
    paginator = Paginator(writing_task_list, 5)
    page = request.GET.get('page')
    try:
        writing_task_list = paginator.page(page)
    except PageNotAnInteger:
        writing_task_list = paginator.page(1)
    except EmptyPage:
        writing_task_list = paginator.page(paginator.num_pages)

    content = {
        'type': type,
        'user': user,
        'state_list': state_list,
        'query_state': query_state,
        'writing_task_list': writing_task_list,
    }
    return render(request, 'writings/my_writing_tasks.html', content)

@user_passes_test(mentor_permission_check)
def get_writing_task(request, d):
    user = request.user if request.user.is_authenticated() else None
    mentorprofile = MentorProfile.objects.get(userprofile=user.userprofile)
    writing_task = WritingTask.objects.get(id=d)
    
    if mentorprofile.isvalid:
        if writing_task.state == 1:
            writing_task.state = 2
            writing_task.editor = mentorprofile
            writing_task.save()
            return HttpResponseRedirect("/writings/mywritingtasks/")

    content = {
        'user': user,
    }
    return render(request, '404.html', content)
