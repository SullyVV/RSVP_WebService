from django.contrib.auth.models import User
from django import forms

class UserForm_register(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label="password", widget=forms.PasswordInput())
    email = forms.EmailField(label="email: ")

class UserForm_login(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label="password", widget=forms.PasswordInput)