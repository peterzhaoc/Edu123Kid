from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from writings.models import *
from writings.forms import *
from django.core.urlresolvers import reverse
from profiles.utils import permission_check
import json

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


def writing_task_detail(request):
    user = request.user if request.user.is_authenticated() else None
    writing_task_id = request.GET.get('id', '')
    if writing_task_id == '':
        return HttpResponseRedirect(reverse('view_writing_task_list'))
    try:
        writing_task = WritingTask.objects.get(pk=writing_task_id)
    except WritingTask.DoesNotExist:
        return HttpResponseRedirect(reverse('view_writing_task_list'))
    content = {
        'user': user,
        'writing_task': writing_task,
    }
    return render(request, 'management/detail.html', content)


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

@user_passes_test(permission_check) 
def add_writing_task(request):
    user = request.user
    state = None
    
    if request.method == 'POST':
        form = WritingTaskForm(request.POST,request.FILES)
        if form.is_valid():
            new_writing_task = WritingTask(
            title=form.cleaned_data['title'],
            writingfile=form.cleaned_data['writingfile'],
            author=user,
            )
            new_writing_task.save()
        return HttpResponseRedirect("/writings/view_writing_task_list/")
    else:
        form = WritingTaskForm()

    content = {
        'user': user,
        'state': state,
        'writing_task_list': WritingTask.objects.all(),
        'form': form,
    }
    return render(request, 'writings/add_writing_task.html', content)

@user_passes_test(permission_check)
def view_writing_task_list(request):
    user = request.user if request.user.is_authenticated() else None
    category_list = WritingTask.objects.values_list('state', flat=True).distinct()
    query_category = request.GET.get('state', 'all')
    if (not query_category) or WritingTask.objects.filter(category=query_category).count() is 0:
        query_category = 'all'
        writing_task_list = WritingTask.objects.all()
    else:
        writing_task_list = WritingTask.objects.filter(category=query_category)
    
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        writing_task_list = WritingTask.objects.filter(name__contains=keyword)
        query_category = 'all'
    
    paginator = Paginator(writing_task_list, 5)
    page = request.GET.get('page')
    try:
        writing_task_list = paginator.page(page)
    except PageNotAnInteger:
        writing_task_list = paginator.page(1)
    except EmptyPage:
        writing_task_list = paginator.page(paginator.num_pages)
    content = {
        'user': user,
        'category_list': category_list,
        'query_category': query_category,
        'writing_task_list': writing_task_list,
    }
    return render(request, 'management/view_book_list.html', content)
