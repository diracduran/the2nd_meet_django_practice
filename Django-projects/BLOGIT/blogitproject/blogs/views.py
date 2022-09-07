from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.models import Blog
from profiles.models import Profile
from comments.models import Comment

# Create your views here.
@login_required
def show_blog(request):
    blogs = Blog.objects.filter(is_published = True)
    context = {
        'blogs': blogs
    }
    return render(request, 'pages/blog.html', context=context)

# @login_required
# def show_all_blogs(request):
#     blogs = Blog.objects.filter(is_published = True)
#     context = {
#         'blogs': blogs
#     }
#     return render(request, 'pages/index.html', context=context)

@login_required
def single_blog(request, author, slug):
    profile = Profile.objects.get(user__username=author)
    blog = Blog.objects.get(author=profile, slug=slug)
    context = {
    'blog': blog,
    'profile': profile,
    }
    return render(request, 'pages/single-blog.html', context=context)