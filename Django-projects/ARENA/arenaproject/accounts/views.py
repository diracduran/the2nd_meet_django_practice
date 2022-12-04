from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
            # messages.success(request, 'Welcome back, {} :>'.format(user.get_username()))
            return redirect('index')
        else:
            # messages.error(request, 'Something is going wrong :<')
            return render(request, 'accounts/login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')