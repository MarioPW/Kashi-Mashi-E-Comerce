from django.urls import path
from .views import *

urlpatterns = [  
    path('register_user/', register_user, name='register_user'),
]