from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^courses/index/$', views.index, name='courses_index'),
    url(r'^courses/detail/(\d+)$', views.coursebase_detail, name='coursebase_detail'),
    url(r'^courses/addcourse/$', views.add_course, name='courses_add_course'),
    url(r'^courses/mycourses/$', views.my_courses, name='courses_my_courses'),
    url(r'^courses/myclasses/$', views.my_classes, name='courses_my_classes'),
]
