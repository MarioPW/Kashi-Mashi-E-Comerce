from django import forms
from .models import Message, Another_Equal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Form_Message(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('id','customer_email', 'message','image')

class Form_Another_Equal(forms.ModelForm):
    class Meta:
        model = Another_Equal
        fields = ('customer_email',)

class Register_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        
