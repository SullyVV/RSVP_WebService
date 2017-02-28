from django import forms
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from .models import Question, Choice, User, Event
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm_register, UserForm_login, EventForm
from .models import User, Event, Answer, Relationship

# Create your views here.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    answers = Answer.objects.filter(event_title=event.title)
    return render(request, 'polls/event.html', {'event':event, "answers":answers})

def event_edit(request, event_id):
    if request.method == "POST":
        uf = EventForm(request.POST)
        if uf.is_valid():
            event_title = uf.cleaned_data['event_title']
            event_time = uf.cleaned_data['event_time']
            event_place = uf.cleaned_data['event_place']
            event_description = uf.cleaned_data['event_description']
            event_plusOne = uf.cleaned_data['event_plusOne']
            event_guests = uf.cleaned_data['event_guests']
            guestList = event_guests.split(";")
            event = Event()
            #update event table
            event.title = event_title
            event.event_time = event_time
            event.place = event_place
            event.descrption = event_description
            event.plusOne = event_plusOne
            #event.save()
            #update relationship table, if user exist, save into relationship
            for guest in guestList:
                if User.objects.filter(username = guest).exists():
                    print(guest + " exists")
                    relation = Relationship()
                    relation.event_title = event_title
                    relation.guest_name = guest
                    relation.isAnswered = False
                    #relation.save()
            #redirect to event page
            return HttpResponseRedirect(reverse('polls:event', args=(event_id,)))
            #return redirect('polls:login')
    else:
        uf = EventForm()
    return render_to_response("polls/event_edit.html", {'uf':uf}, RequestContext(request))


def answer(request, answer_id):
    answer = get_object_or_404(Event, pk=answer_id)
    return HttpResponse("answer" + str(answer_id))
    return render(request, 'polls/answer.html', {'answer':answer})

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list,})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def user(request, userid):
    user = get_object_or_404(User, pk=userid)
    event_created = Event.objects.filter(owner_name = user.username)
    answer_made = Answer.objects.filter(answer_name = user.username)
    return render(request, 'polls/userevents.html', {'username':user.username,'event_created': event_created, 'answer_made':answer_made})
    # show all event of current user and put a plus button for it to add new event, traverse through entire database and show events



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
                userid = User.objects.get(username = username).id
                return HttpResponseRedirect(reverse('polls:user', args=(userid,)))
            else:
                return render_to_response('polls/login.html', {'uf':uf})
    else:
        uf = UserForm_login()
    return render_to_response('polls/login.html', {'uf':uf})