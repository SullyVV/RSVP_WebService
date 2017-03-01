from django.contrib.auth.models import User
from django import forms

class UserForm_register(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label="password", widget=forms.PasswordInput())
    email = forms.EmailField(label="email: ")

class UserForm_login(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label="password", widget=forms.PasswordInput)

class EventForm(forms.Form):
    event_title = forms.CharField(label="event title", max_length=200)
    event_time = forms.CharField(label="event date(02/20/2017)", max_length=100)
    event_place = forms.CharField(label="event place", max_length=100)
    event_description = forms.CharField(label="event description", max_length=200)
    event_guests = forms.CharField(label="event guests (e.g. Jack;John;Lucy)", max_length=200)
    event_vender = forms.CharField(label="event vender", max_length=50)
    event_plusOne = forms.BooleanField(label="Can bring more than one person", required=False)
    event_venderPermitted = forms.BooleanField(label="Is vender permitted to see the response?", required=False)

class EventEditForm(forms.Form):
    event_time = forms.CharField(label="event date(02/20/2017)", max_length=100)
    event_place = forms.CharField(label="event place", max_length=100)
    event_description = forms.CharField(label="event description", max_length=200)
    event_newGuests = forms.CharField(label="add new guests (e.g. Jack;John;Lucy)", max_length=200)
    event_plusOne = forms.BooleanField(label="Can bring more than one person", required=False)
    event_venderPermitted = forms.BooleanField(label="Is vender permitted to see the response?", required=False)



class AnswerForm(forms.Form):
    comment = forms.CharField(label="comment (e.g. Any food allergy, seat preference ?)", max_length=200)
    willCome = forms.BooleanField(label="I will come", required=False)
    plusOne = forms.BooleanField(label="I will bring people with me", required=False)

class FinalForm(forms.Form):
    final = forms.BooleanField(label="Final", required=False)