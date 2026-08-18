from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Episodes, User, WatchHistory


def registration_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            messages.error(request, 'Пароли не совпадают')
            return render(request, 'register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует')
            return render(request, 'register.html')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        login(request, user)
        messages.success(request, 'Регистрация прошла успешно')
        return redirect('home')
    
    return render(request, 'registration.html')
    
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы вошли в аккаунт')
            return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
    
    return render(request, 'login.html')
    
    
def logout_user(request):
    logout(request)
    messages.info(request, "Вы вышли из аккаунта")
    return redirect("home")

#--------------------------------------------------#
def home_page(request):
    episodes = Episodes.objects.all()
    
    
    
    return render(request, "home.html")
    

def wiki_page(request):
    return render(request, "wiki.html")



def player_page(request):
    return render(request, "player.html")



def profile_page(request):
    return render(request, "profile.html")


