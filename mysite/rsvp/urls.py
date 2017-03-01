from django.conf.urls import url
from . import views
app_name = 'rsvp'
urlpatterns = [
    #/rsvp/
    url(r'^$', views.index, name='index'),
    #/rsvp/register/,
    url(r'^register/$', views.register, name='register'),
    #/login/,
    url(r'^login/$', views.login, name='login'),
    #/user/admin,
    url(r'^user/(?P<userid>[0-9]+)/$', views.user, name='user'),
    #/rsvp/event/5
    url(r'^event/(?P<event_id>[0-9]+)/$', views.event, name='event'),
    #/rsvp/event/create/5(user_id)
    url(r'^event/create/(?P<user_id>[0-9]+)/$', views.event_create, name='event_create'),
    #/rsvp/event/5/edit
    url(r'^event/(?P<event_id>[0-9]+)/edit/$', views.event_edit, name='event_edit'),
    #/rsvp/answer/5/
    url(r'^answer/(?P<answer_id>[0-9]+)/$', views.answer, name='answer'),
    #/rsvp/answer/5/edit/
    url(r'^answer/(?P<answer_id>[0-9]+)/edit/$', views.answer_edit, name='answer_edit'),
    #/rsvp/answer/create/5(event_id)/5(user_id)
    url(r'^answer/create/(?P<relation_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.answer_create, name='answer_create'),
    #/rsvp/vender/5(vender_id)
    url(r'^vender/(?P<vender_id>[0-9]+)/$', views.vender, name='vender'),
    #/rsvp/send/
    url(r'^send/$', views.send, name='send'),
]