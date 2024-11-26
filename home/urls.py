from django.urls import path
from .views import *

urlpatterns = [  
    path('', home, name='home'),
    path('index/', home, name='home'),
    path('message/', message, name='message'),
    path('orders/<int:id>', orders, name='orders'),
    path('frequent_questions/', frequent_questions, name='questions'),
    path('payment_methods/', payment_methods, name='payment_methods'),
    path('another_equal/<int:id>', another_equal, name='another_equal'),
    path('register_user/', register_user, name='register_user'),
]