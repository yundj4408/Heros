from django.urls import path
from .views import *

app_name = 'employee'

urlpatterns = [
    path('',employee_all, name='employee_all'),
    path('new/',new_feed, name='new_feed'),
    path('feed/<pk>/', detail_feed),
    path('feed/<pk>/remove/', remove_feed),
    path('feed/<pk>/edit/', edit_feed),
]

