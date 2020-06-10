from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

# Create your views here.
def signup_view(request): # 회원가입 화면을 위한 뷰
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
        return redirect('/')
    else:
        signup_form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'signup_form':signup_form})


def login_view(request): # 로그인 화면 뷰
    if request.method =="POST":
        login_form = LoginForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('/')
        else:
            messages.info(request,'다시 로그인해 주세요')
            return render(request, 'accounts/login.html', {'login_form': login_form})

    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form': login_form})

def logout_view(request): #로그아웃 화면 뷰
    auth.logout(request)
    return redirect('/')

def people(request, id): # 회원정보 뷰
    people = get_object_or_404(get_user_model(), id = id)
    return render(request, 'accounts/people.html', {'people':people})

def update(request): # 회원정보 수정 뷰
    if request.method =="POST":
        change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if change_form.is_valid():
            change_form.save()
            return redirect('/')
        return render(request, 'accounts/update.html',{'change_form':change_form, 'r_test':request.user})

    else:
        change_form = CustomUserChangeForm(request.POST)
        return render(request, 'accounts/update.html',{'change_form':change_form})

def delete(request): # 회원삭제 뷰
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('/')

    return render(request, 'accounts/delete.html')



def change_pw(request): #비밀번호 변경 뷰
    context= {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password,user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.login(request,user)
                return redirect('/')
            else:
                context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
        else:
            context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

    return render(request, "accounts/change_pw.html",context)
