from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^home/index/$', views.index, name='homeindex'),
    url(r'^home/success/$',views.success),
]
