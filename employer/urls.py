from django.urls import path

from .views import *

app_name = 'employer'

urlpatterns = [
    path('', employer_all, name='employer_all'),
]