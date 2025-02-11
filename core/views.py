from django.shortcuts import render, redirect 
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# Create your views here.

def Home_View(request):
    return render(request, 'home.html')

def Register_View(request):
    registerform = UserCreationForm()
    if request.method == 'POST':
        registerform = UserCreationForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            return redirect('login')
    else:
        registerform = UserCreationForm()
    
    return render(request, 'register.html', {'registerform':registerform})

def Login_View(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
                login(request, user)
                return redirect('profile')
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
        
            
    return render(request, 'login.html')

@login_required
def Profile_View(request):
    return render(request, 'profile.html')

def Logout_View(request):
    logout(request) 
    return render(request, 'logout.html')