from django.conf.urls import url, include
from django.contrib.staticfiles import views
from django.contrib import admin
from django.conf import settings
from Edu123Kid.views import *

urlpatterns = [
    #url('', include('social_django.urls', namespace='social'))
    url(r'^admin/', admin.site.urls),
    url(r'^test/', test, name='test'),
    url(r'', include('home.urls')),
    url(r'', include('writings.urls')),
    url(r'', include('profiles.urls')),
    url(r'', include('courses.urls')),
    #url(r'^captcha/', include('captcha.urls')),
    url(r'^getVaptcha/', get_vaptcha),
    url(r'^validate/', validate),
]

if not settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.static.serve, {'document_root': settings.STATIC_ROOT}, name="static"),
        url(r'^media/(?P<path>.*)$', views.static.serve, {'document_root': settings.MEDIA_ROOT}, name="media")
    ]
else:
    import debug_toolbar
    urlpatterns += [
                    url(r'^__debug__/', include(debug_toolbar.urls)),
                    url(r'^static/(?P<path>.*)$', views.static.serve, {'document_root': settings.STATIC_ROOT}, name="static"),
                    url(r'^media/(?P<path>.*)$', views.static.serve, {'document_root': settings.MEDIA_ROOT}, name="media")
                    ]
