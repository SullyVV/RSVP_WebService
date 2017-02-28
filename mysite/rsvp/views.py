from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect


from django.urls import reverse
# Create your views here.
def userinfo(request):
    return HttpResponse("at user info page")
