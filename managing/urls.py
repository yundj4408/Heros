from django.urls import path

from .views import *

app_name = 'managing'

urlpatterns = [
    path('', Notice_all, name='Notice_all'),
    path('FAQ/',FAQ_all,name='FAQ_all')
]