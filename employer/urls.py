from django.urls import path

from .views import *

app_name = 'employer'

#views.py기능과 url연결
urlpatterns = [
    path('',employer_all, name='employer_all'),
    path('new/',new_feed, name='new_feed'),
    path('feed/<pk>/', detail_feed),
    path('feed/<pk>/remove/', remove_feed),
    path('feed/<pk>/edit/', edit_feed),
    path('home/', sort1, name='home'),
    path('load/',sort2, name='load'),
    path('pet/',sort3, name='pet'),
    path('acting/',sort4, name='acting'),
    path('short/',sort5, name='short'),
    path('carpool/',sort6, name='carpool'),
    path('etc/',sort7, name='etc'),
]