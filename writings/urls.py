from django.conf.urls import url
from writings import views

urlpatterns = [
    url(r'^writings/add_img/$', views.add_img, name='add_img'),
    url(r'^writings/add_book/$', views.add_book, name='add_book'),
    url(r'^writings/add_writing_task/$', views.add_writing_task, name='add_writing_task'),
    url(r'^writings/view_writing_task_list/$', views.view_writing_task_list, name='view_writing_task_list'),
    url(r'^writings/view_writing_task/detail/$', views.writing_task_detail, name='writing_task_detail'),
    url(r'^writings/view_book_list/$', views.view_book_list, name='view_book_list'),
]
