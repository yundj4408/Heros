from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.
def mypage_detail(request):
    return render(request, 'mypage/mypage_detail.html')


