from django.urls import path
from .views import *
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view'),
    path('login/', login_view, name='login_view'),
    path('people/<str:id>/', people, name='people'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),
    path('change_pw/',change_pw, name='change_pw'),
]