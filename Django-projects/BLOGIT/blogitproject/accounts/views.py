from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from profiles.models import Profile
from accounts.tasks import send_email_reset_password_task
import uuid

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
    messages.success(request, 'Good Bye 👋🏻')
    return redirect('login')

def forgot_password(request):
    if request.user.is_authenticated:
        messages.success(request, "You're authenticated, so you can't use 'forgot password' option")
        return redirect('index')

    if request.method == 'GET':
        return render(request, 'accounts/forgot_password.html')

    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'Something is going wrong :<')
            return render(request, 'accounts/forgot_password.html')
        else:
            profile = Profile.objects.get(user=user)
            reset_link = profile.reset_password_link_uuid
            subject = 'Reset Password'
            message = f'✨ Here your reset password link: {reset_link} ✨'
            send_email_reset_password_task(subject=subject, message=message, email=email)
            messages.success(request, f'Email has been sent to your address: {email}')
            return redirect('forgot_password')

def change_password(request, reset_password_link_uuid):
    if request.user.is_authenticated:
        messages.success(request, "You're authenticated, so you can't use 'change password' option")
        return redirect('index')

    if request.method == 'GET':
        return render(request, 'accounts/change_password.html')

    try:
        profile = Profile.objects.get(reset_password_link_uuid=reset_password_link_uuid)
    except:
        messages.error(request, 'Something is going wrong :<')
        return render(request, 'accounts/change_password.html')
    else:
        user = profile.user

    if request.method == 'POST':
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            user.set_password(password)
            user.save()
            # обновление ссылки после смены пароля
            profile.reset_password_link_uuid = uuid.uuid4()
            profile.save
            messages.success(request, f'You changed password✨')
            return redirect('login')
        else:
            messages.error(request, 'Passwords did not match :<')
            return render(request, 'accounts/change_password.html')