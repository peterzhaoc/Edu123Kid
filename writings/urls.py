from django.conf.urls import url
from writings import views

urlpatterns = [
    url(r'^writings/best/$', views.best, name='best'),
    url(r'^writings/add_img/$', views.add_img, name='add_img'),
    url(r'^writings/add_book/$', views.add_book, name='add_book'),
    url(r'^writings/add_writing_task/$', views.add_writing_task, name='add_writing_task'),
    url(r'^writings/distribute_writing_task/(\d+)$', views.distribute_writing_task, name='distribute_writing_task'),
    url(r'^writings/view_writing_task_list/$', views.view_writing_task_list, name='view_writing_task_list'),
    url(r'^writings/writingtask/detail/(\d+)$', views.writing_task_detail, name='writingtaskdetail'),
    url(r'^writings/view_book_list/$', views.view_book_list, name='view_book_list'),
    url(r'^writings/mywritingtasks/$', views.my_writing_tasks, name='my_writing_tasks'),
    url(r'^writings/get_writing_task/(\d+)$', views.get_writing_task),
]
