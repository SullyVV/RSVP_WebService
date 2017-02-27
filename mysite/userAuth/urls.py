from django.conf.urls import url
from . import views
app_name = 'userAuth'
urlpatterns = [
    #/userAuth/
    url(r'^$', views.index, name='index'),
    #/userAuth/checkUser
    url(r'^checkUser/$', views.checkUser, name='checkUser'),
    #/userAuth/info
    url(r'^info/$', views.info, name='info'),
    #/userAuth/register
    url(r'^register/$', views.register, name='register'),
    #/polls/
    #url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]