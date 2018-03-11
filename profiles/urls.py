from django.conf.urls import url
from profiles import views

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^profiles/userprofile/$', views.user_profile, name='user_profile'),
    url(r'^profiles/signup/$', views.signup, name='signup'),
    url(r'^profiles/login/$', views.login, name='login'),
    url(r'^profiles/logout/$', views.logout, name='logout'),
    url(r'^profiles/set_password/$', views.set_password, name='set_password'),
    url(r'^profiles/get_verification_code/$', views.get_verification_code, name='get_verification_code'),
]
