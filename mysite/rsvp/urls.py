from django.conf.urls import url
from . import views
app_name = 'rsvp'
urlpatterns = [
    #/userAuth/
    #url(r'^$', views.index, name='index'),
    #/userAuth/checkUser
    #url(r'^checkUser/$', views.checkUser, name='checkUser'),
    #/userAuth/info
    #url(r'^(?P<username>)/userinfo/$', views.userinfo, name='userinfo'),
    url(r'^userinfo/$', views.userinfo, name='userinfo'),
    #/userAuth/register
    #url(r'^register/$', views.register, name='register'),
]