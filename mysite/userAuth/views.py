from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import User
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'userAuth/index.html', {})
def info(request):
    return render(request, 'userAuth/info.html',{})
def checkUser(request):
    username = request.POST['username']
    password = request.POST['password']
    stored_pswd = User.objects.get(user_name = username)
    print(password)
    print(stored_pswd)
    if (str(password) == str(stored_pswd)):
        #go to user page
        return HttpResponse("go to user page")
    else:
        #go to main login page
        return render(request, "userAuth/index.html", {})
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    new_user = User(user_name=username, user_password=password, user_email=email)
    new_user.save()
    return render(request, "userAuth/index.html", {})