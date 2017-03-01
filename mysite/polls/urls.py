from django.conf.urls import url
from . import views
app_name = 'polls'
urlpatterns = [
    #/polls/
    url(r'^$', views.index, name='index'),
    #/register/,
    url(r'^register/$', views.register, name='register'),
    #/login/,
    url(r'^login/$', views.login, name='login'),
    #/user/admin,
    url(r'^user/(?P<userid>[0-9]+)/$', views.user, name='user'),
    #/polls/event/5
    url(r'^event/(?P<event_id>[0-9]+)/$', views.event, name='event'),
    #/polls/event/create/5(user_id)
    url(r'^event/create/(?P<user_id>[0-9]+)/$', views.event_create, name='event_create'),
    #/polls/event/5/edit
    url(r'^event/(?P<event_id>[0-9]+)/edit/$', views.event_edit, name='event_edit'),
    #/polls/answer/5/
    url(r'^answer/(?P<answer_id>[0-9]+)/$', views.answer, name='answer'),
    #/polls/answer/5/edit/
    url(r'^answer/(?P<answer_id>[0-9]+)/edit/$', views.answer_edit, name='answer_edit'),
    #/polls/answer/create/5(event_id)/5(user_id)
    url(r'^answer/create/(?P<relation_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.answer_create, name='answer_create'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]