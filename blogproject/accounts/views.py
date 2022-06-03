from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    # POST 요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST':
        userid = request.POST['username']
        password = request.POST['password']
        username = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    # GET 요청이 들어오면 login form 을 달고있는 login.html을 띄워주는 역할
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')