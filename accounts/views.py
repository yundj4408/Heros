from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


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
        login_form = LoginForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
        return redirect('/')

    else:
        login_form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'login_form': login_form})

def logout_view(request):
    auth.logout(request)
    return redirect('/')

def people(request, name):
    people = get_object_or_404(get_user_model(), name = name)
    return render(request, 'accounts/people.html', {'people':people})

def update(request):
    if request.method =="POST":
        change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if change_form.is_vaild():
            change_form.save()
            return redirect('accounts:people', request.user.name)

    else:
        change_form = CustomUserChangeForm(request.POST)
        return render(request, 'accounts/update.html',{'change_form':change_form})

@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('/')
    return render(request, 'accounts/delete.html')
