from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (authenticate,
                                 logout as app_logout,
                                 login as app_login)


def login(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            app_login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username/password. Please, try again")
    return redirect("login")


def logout(request):
    app_logout(request)
    return redirect('login')
