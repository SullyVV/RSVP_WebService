import datetime
from django.utils import timezone
from django import forms
from django.db.models.functions import datetime
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from .models import Question, Choice, User, Event
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm_register, UserForm_login, EventForm, AnswerForm, FinalForm, EventEditForm
from .models import User, Event, Answer, Relationship, Vender
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    answers = Answer.objects.filter(event_title=event.title)
    relations = Relationship.objects.filter(event_title=event.title)
    return render(request, 'polls/event.html', {'event':event, "answers":answers, "relations":relations})


def event_create(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        ef = EventForm(request.POST)
        if ef.is_valid():
            event_title = ef.cleaned_data['event_title']
            event_time = ef.cleaned_data['event_time']
            event_place = ef.cleaned_data['event_place']
            event_description = ef.cleaned_data['event_description']
            event_guests = ef.cleaned_data['event_guests']
            event_plusOne = ef.cleaned_data['event_plusOne']
            event_vender = ef.cleaned_data['event_vender']
            event_venderPermitted = ef.cleaned_data['event_venderPermitted']
            event = Event()
            event.created_by = user
            event.owner_name = user.username
            event.title = event_title
            event.descrption = event_description
            event.event_time = event_time
            event.vender_name = event_vender
            event.place = event_place
            event.plusOne = event_plusOne
            event.venderPermitted = event_venderPermitted
            event.save()
            #create relations for this event
            guestList = event_guests.split(";")
            for guest in guestList:
                relation = Relationship()
                relation.event_title = event_title
                relation.guest_name = guest
                relation.isAnswered = False
                relation.save()
            to_email = []
            subject = "New invitation from RSVP.com"
            from_email = settings.EMAIL_HOST_USER
            contact_msg = "Hey, You have pending invitations at RSVP web app"
            for guest in guestList:
                user = get_object_or_404(User, username = guest)
                to_email.append(user.email)
            # send to all guests
            print(to_email)
            send_mail(subject, contact_msg, from_email, to_email, fail_silently=False)
            #create vender relationship for this event
            vender_user = get_object_or_404(User, username=event_vender)
            vender = Vender()
            vender.event = event
            vender.event_title = event_title
            vender.vender = vender_user
            vender.vender_name = vender_user.username
            vender.save()
            return HttpResponseRedirect(reverse('polls:user', args=(user_id,)))
            # return redirect('polls:login')
    else:
        ef = EventForm()
    return render_to_response("polls/event_create.html", {'ef': ef}, RequestContext(request))


def vender(request, vender_id):
    vender_relation = get_object_or_404(Vender, pk=vender_id)
    event = vender_relation.event
    vender = vender_relation.vender
    answers = Answer.objects.filter(event_title=event.title)
    relations = Relationship.objects.filter(event_title=event.title)
    if request.method == "POST":
        ff = FinalForm(request.POST)
        if ff.is_valid():
            isFinal = ff.cleaned_data['final']
            if isFinal:
                #update event table
                event.isFinal = isFinal
                event.save()
                #update answer for this event
                for answer in answers:
                    answer.isEditable = False
                    answer.save()
                #update relationship table, all relationship on about this event should be marked as finalized
                relations = Relationship.objects.filter(event_title = event.title)
                for relation in relations:
                    relation.isFinal = isFinal
                    relation.save()
            #redirect to vender's page
            return HttpResponseRedirect(reverse('polls:user', args=(vender.id,)))
    else:
        ff = FinalForm()
    return render_to_response("polls/vender.html", {'ff':ff, 'event':event, 'answers':answers, 'relations':relations}, RequestContext(request))





def event_edit(request, event_id):
    if request.method == "POST":
        uf = EventEditForm(request.POST)
        if uf.is_valid():
            event_time = uf.cleaned_data['event_time']
            event_place = uf.cleaned_data['event_place']
            event_description = uf.cleaned_data['event_description']
            event_plusOne = uf.cleaned_data['event_plusOne']
            event_newGuests = uf.cleaned_data['event_newGuests']
            event_venderPermitted = uf.cleaned_data['event_venderPermitted']
            newguestList = event_newGuests.split(";")
            event = get_object_or_404(Event, pk=event_id)
            #update event table
            event.event_time = event_time
            event.place = event_place
            event.descrption = event_description
            event.plusOne = event_plusOne
            event.venderPermitted = event_venderPermitted
            event.save()
            #update relationship table, if user exist, save into relationship
            for guest in newguestList:
                if User.objects.filter(username = guest).exists():
                    print(guest + " exists")
                    relation = Relationship()
                    relation.event_title = event.title
                    relation.guest_name = guest
                    relation.isAnswered = False
                    relation.save()
            to_email = []
            subject = "New invitation from RSVP.com"
            from_email = settings.EMAIL_HOST_USER
            contact_msg = "Hey, You have pending invitations at RSVP web app"
            for guest in newguestList:
                user = get_object_or_404(User, username=guest)
            to_email.append(user.email)
            # send to all guests
            print(to_email)
            send_mail(subject, contact_msg, from_email, to_email, fail_silently=False)
            #redirect to event page
            return HttpResponseRedirect(reverse('polls:event', args=(event_id,)))
    else:
        uf = EventEditForm()
    return render_to_response("polls/event_edit.html", {'uf':uf}, RequestContext(request))


def answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    return render(request, 'polls/answer.html', {'answer':answer})

def answer_edit(request, answer_id):
    if request.method == "POST":
        af = AnswerForm(request.POST)
        if af.is_valid():
            comment = af.cleaned_data['comment']
            plusOne = af.cleaned_data['plusOne']
            willCome = af.cleaned_data['willCome']
            answer = get_object_or_404(Answer, pk = answer_id)
            answer.comment = comment
            answer.plusOne = plusOne
            answer.willCome = willCome
            answer.save()
            #redirect to event page
            return HttpResponseRedirect(reverse('polls:answer', args=(answer_id,)))
            #return redirect('polls:login')
    else:
        af = AnswerForm()
    return render_to_response("polls/answer_edit.html", {'af':af}, RequestContext(request))


def answer_create(request, relation_id, user_id):
    relation = get_object_or_404(Relationship, pk=relation_id)
    event = get_object_or_404(Event, title=relation.event_title)
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        af = AnswerForm(request.POST)
        if af.is_valid():
            comment = af.cleaned_data['comment']
            plusOne = af.cleaned_data['plusOne']
            willCome = af.cleaned_data['willCome']
            answer = Answer()
            answer.event = event
            answer.event_title = event.title
            answer.answered_by = user
            answer.answer_name = user.username
            #answer.data = datetime.date.now()
            answer.comment = comment
            answer.plusOne = plusOne
            answer.willCome = willCome
            answer.save()
            #mark relation as answered
            relation.isAnswered = True
            relation.save()
            #redirect to event page with answer id
            answer = Answer.objects.filter(event_title = event.title).last()
            print(answer.answer_name)
            return HttpResponseRedirect(reverse('polls:answer', args=(answer.id,)))
            #return redirect('polls:login')
    else:
        af = AnswerForm()
    return render_to_response("polls/answer_create.html", {'event':event,'af':af}, RequestContext(request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list,})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def user(request, userid):
    user = get_object_or_404(User, pk=userid)
    event_created = Event.objects.filter(owner_name = user.username)
    event_invited = Relationship.objects.filter(guest_name = user.username)
    answer_made = Answer.objects.filter(answer_name = user.username)
    vender_relation = Vender.objects.filter(vender_name = user.username)
    return render(request, 'polls/userevents.html',
                  {'user': user, 'event_created': event_created, 'event_invited': event_invited, 'answer_made':answer_made, 'vender_relation':vender_relation})
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

def send(request):
    subject = "Site contact form"
    from_email = settings.EMAIL_HOST_USER
    to_email = ['johndong9317@gmail.com', 'gd50@gmail.com', 'AmberWangjie@gmail.com']
    contact_msg = "check out rsvp app"
    send_mail(subject, contact_msg, from_email, to_email, fail_silently=False)
    return HttpResponse("on send email page")