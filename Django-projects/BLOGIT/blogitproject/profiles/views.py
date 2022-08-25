from django.shortcuts import render, get_object_or_404, redirect
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def get_user_profile(request, username):
    if request.method == 'GET':
        profile = get_object_or_404(Profile, user__username=username)
        # profile = Profile.objects.get(user__username=username)
        context = {
            'profile': profile,
        }
        return render(request, 'profiles/profile.html', context=context)


@login_required
def edit_user_profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    context = {
        'profile': profile,
    }
    if request.method == 'GET':
        if request.user.id == profile.user.id:
            return render(request, 'profiles/edit_profile.html', context=context)
    else:
        return render(request, 'profiles/profile.html', context=context)

    if request.method == 'POST':
        user = request.user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        status = request.POST['status']
        about = request.POST['about']
        # user update
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        # profile update
        profile.status = status
        profile.about = about
        # profile image update
        try:
            if any(request.FILES):
                profile.profile_image = request.FILES['profile_image']
                profile.is_thumbnailed = False
        except:
            return render(request, 'profiles/edit_profile.html', context=context)
        # profile and user save
        user.save()
        profile.save()
        messages.success(request, 'Profile is edited :>')
        return render(request, 'profiles/profile.html', context=context)