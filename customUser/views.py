from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserLoginForm, UserRegistrationForm
from .models import User

# Create your views here.
def user_register(request):
    if request.method == "GET":
        return render(request, 'customUser/register.html', {"form": UserRegistrationForm()})
    if request.method == "POST":
        # Make bounded form
        bounded_form = UserRegistrationForm(request.POST)
        # Check if valid
        if bounded_form.is_valid():
            # Extract username and password
            username = bounded_form.cleaned_data['username']
            password = bounded_form.cleaned_data['password1']

            new_user = User.objects.create_user(username=username, password=password)
            print(new_user)
            return HttpResponse('SUCCESS')
    
        return HttpResponse('FAILURE')


def user_login(request):
    if request.method == "GET":
        return render(request, 'customUser/login.html', {"form": UserLoginForm()})
    if request.method == "POST":
        bounded_user_login_form = UserLoginForm(request.POST)
        if bounded_user_login_form.is_valid():
            username = bounded_user_login_form.cleaned_data['username']
            password = bounded_user_login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('SUCCESS')
            else:
                return HttpResponse("Wrong username or password")
        else:
            return HttpResponse(bounded_user_login_form.errors)
    

def user_logout(request):
    logout(request)
    return HttpResponse('You have been logged out')


