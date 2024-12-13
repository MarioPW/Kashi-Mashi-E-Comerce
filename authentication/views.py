from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
def register_user(request):   

    if request.method == 'POST':
        new_user = UserCreationForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            username = new_user.cleaned_data['username']
            password = new_user.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            message = f'{username.capitalize()}'
            return render(request, 'index.html', {'alert': message})
        else:
            message = f'Opps! Parece que algo salió mal...'
            return render(request,'register_user.html', {'alert': message})
    else:       
        return render(request, 'register_user.html')

def logout_user(request):
    logout(request)
    return render(request, 'index.html')

def login_user(request):
    return render(request, 'login_user.html')
