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
    #url(r'^(?P<question_id>[0-9]+)/user/$', views.user, name='user'),
    url(r'^user/(?P<userid>[0-9]+)$', views.user, name='user'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]