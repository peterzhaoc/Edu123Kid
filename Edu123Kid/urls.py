from django.conf.urls import url, include
from django.contrib.staticfiles import views
from django.contrib import admin
from django.conf import settings
from profiles.views.index as index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'', include('writings.urls')),
    url(r'', include('profiles.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.static.serve, {'document_root': settings.STATIC_ROOT}, name="static"),
        url(r'^media/(?P<path>.*)$', views.static.serve, {'document_root': settings.MEDIA_ROOT}, name="media")
    ]
