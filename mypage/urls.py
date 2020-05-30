from django.urls import path

from .views import *

app_name = 'mypage'

urlpatterns = [
    path('', mypage_detail, name='mypage_detail'),
]