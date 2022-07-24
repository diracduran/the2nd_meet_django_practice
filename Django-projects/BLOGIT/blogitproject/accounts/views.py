from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome back, {} :>'.format(user.get_username()))
            return redirect('index')
        else:
            messages.error(request, 'Something is going wrong :<')
            return render(request, 'accounts/login.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'accounts/signin.html')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
            except Exception as err:
                messages.error(request, 'Invalid data :<')
                return render(request, 'accounts/signin.html')
            else:
                auth.login(request, user)
                messages.success(request, 'Welcome to BLOGIT APP, {} :>'.format(user.get_username()))
                return redirect('index')
        else:
            messages.error(request, 'Passwords did not match :<')
            return render(request, 'accounts/signin.html')

    return render(request, 'accounts/signin.html')

def logout(request):
    auth.logout(request)
    return redirect('login')