from dataclasses import fields
from django import forms
from .models import User  

from django.contrib.auth.forms import UserCreationForm  

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': "form-control", 'type': "password"}))

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']