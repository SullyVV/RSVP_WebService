from django import forms
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from .models import Question, Choice, User
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm_register, UserForm_login


# Create your views here.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list,})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def user(request, userid):
    user = get_object_or_404(User, pk=userid)
    return HttpResponse("this is the homepage for user: " + userid)
    # show all event of current user and put a plus button for it to add new event



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def register(request):
    if request.method == "POST":
        uf = UserForm_register(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data["username"]
            password = uf.cleaned_data["password"]
            email = uf.cleaned_data["email"]
            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.save()
            #redirect to login page
            return redirect('polls:login')
    else:
        uf = UserForm_register()
    return render_to_response("polls/register.html", {'uf':uf}, RequestContext(request))



def login(request):
    if (request.method == 'POST'):
        uf = UserForm_login(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username = username, password = password)
            if user:
                #return render_to_response('polls/success.html', {'username':username})
                #redirect to user page by userid
                userid = User.objects.get(username = username)
                return HttpResponseRedirect(reverse('polls:user', args=(userid,)))
            else:
                return render_to_response('polls/login.html', {'uf':uf})
    else:
        uf = UserForm_login()
    return render_to_response('polls/login.html', {'uf':uf})