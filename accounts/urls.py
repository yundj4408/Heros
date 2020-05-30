from django.urls import path
from .views import *
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view'),
    path('login/', login_view, name='login_view'),
]