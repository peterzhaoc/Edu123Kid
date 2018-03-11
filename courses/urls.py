from django.conf.urls import url
from courses import views

urlpatterns = [
    url(r'^courses/index/$', views.index, name='courses_index'),

]
