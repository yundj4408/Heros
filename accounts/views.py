from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


# Create your views here.
def signup_view(request):
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
        return redirect('/')
    else:
        signup_form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'signup_form':signup_form})


def login_view(request):
    if request.method =="POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
        return redirect('/')

    else:
        login_form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'login_form': login_form})

def logout_view(request):
    auth.logout(request)
    return redirect('/')

