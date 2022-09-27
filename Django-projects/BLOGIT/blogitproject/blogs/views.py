from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blogs.models import Blog
from profiles.models import Profile
from comments.models import Comment
from django.contrib import messages
from django.http import HttpResponse
import json

# Create your views here.

#blogs
@login_required
def show_blog(request):
    blogs = Blog.objects.filter(is_published = True)
    context = {
        'blogs': blogs
    }
    return render(request, 'pages/blog.html', context=context)

@login_required
def single_blog(request, author, slug):
    profile = Profile.objects.get(user__username=author)
    blog = Blog.objects.get(author=profile, slug=slug)
    context = {
    'blog': blog,
    'profile': profile,
    }
    return render(request, 'pages/single-blog.html', context=context)

@login_required
def create_blog(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    categories = [category[0] for category in Blog.CATEGORY_CHOICE]
    
    context = {
        'profile': profile,
        'categories': categories,
    }

    if request.method == 'GET':
        return render(request, 'pages/create-blog.html', context=context)
    
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        category = request.POST['category']
        tags = request.POST['tags']
        
        # create blog
        blog = Blog()
        blog.title = title
        blog.text = text
        blog.category = category
        blog.author = profile
        try:
            if any(request.FILES):
                blog.image = request.FILES['image']
        except:
            return render(request, 'pages/create-blog.html', context=context)
        blog.save()
        # tags
        if tags:
            tags = tags.replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '').split(',')
            for tag in tags:
                blog.tags.add(tag)
        
        
        return redirect(show_blog)

@login_required
def edit_blog(request, author, slug):
    if author != request.user.username:
        messages.error(request, "It's not your blog!!! You can't edit what is not your's!!!")
        return render('index')
    
    user = request.user
    profile = Profile.objects.get(user=user)
    categories = [category[0] for category in Blog.CATEGORY_CHOICE]
    blog = get_object_or_404(Blog, author=profile, slug=slug)
    
    context = {
        'profile': profile,
        'categories': categories,
        'blog': blog,
    }

    if request.method == 'GET':
        return render(request, 'pages/edit-blog.html', context=context)
    
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        category = request.POST['category']
        tags = request.POST['tags']
        is_published = bool(request.POST.get('is_published', False))
        # edit blog
        blog.title = title
        blog.text = text
        blog.category = category
        blog.is_published = is_published
        # tags
        if tags:
            blog.tags.clear()
            tags = tags.replace(' ', '').replace('\r', '').replace('\t', '').replace('\n', '').split(',')
            for tag in tags:
                blog.tags.add(tag)
        try:
            if any(request.FILES):
                blog.image = request.FILES['image']
        except:
            return render(request, 'pages/create-blog.html', context=context)
        blog.save()
        return redirect('/blogs/blog/{0}/{1}/view'.format(author, blog.slug))


@login_required
def delete_blog(request, author, slug):
    if author != request.user.username:
        messages.error(request, "It's not your blog!!! You can't delete what is not your's!!!")
        return render('show_blog')
    
    user = request.user
    profile = Profile.objects.get(user=user)
    categories = [category[0] for category in Blog.CATEGORY_CHOICE]
    blog = get_object_or_404(Blog, author=profile, slug=slug)
    
    context = {
        'profile': profile,
        'categories': categories,
        'blog': blog,
    }

    if request.method == 'GET':
        blog.delete()
        messages.success(request, "Your blog has been deleted!")
        return redirect('show_blog')


#comments
@login_required
def leave_comment_to_blog(request, author, slug):
    user = request.user
    profile = Profile.objects.get(user=user)
    blog = get_object_or_404(Blog, author__user__username=author, slug=slug)

    if request.method == 'POST':
        # Create comment
        comment = Comment()
        comment.text = request.POST.get('text')
        comment.author = profile
        comment.save()

        # Add comment to existent blog
        blog.comments.add(comment)

        messages.success(request, 'Your comment successfully posted!')
        return redirect('single_blog', author=author, slug=slug)

@login_required
def delete_comment(request, blog_id, comment_id):
    comment = Comment.objects.get(id=str(comment_id))
    comment.delete()
    return redirect('single_blog', blog_id=blog_id)


#likes
@login_required
def add_or_remove_like_to_blog(request, author, slug):
    user = request.user
    blog = get_object_or_404(
        Blog,
        author__user__username=author,
        slug=slug
    )
    profile = Profile.objects.get(user=user)

    # Check profile id in likes list
    if profile.id in blog.likes:
        blog.likes.remove(profile.id)
    else:
        blog.likes.append(profile.id)
    blog.save()
    return redirect('single_blog', author=author, slug=slug)


@login_required
def add_or_remove_like_ajax(request):
    if request.is_ajax():
        user = request.user
        blog_id = request.POST.get('blog_id')
        blog = Blog.objects.get(id=blog_id)
        profile = Profile.objects.get(user=user)

        # Check profile id in likes list
        if profile.id in blog.likes:
            blog.likes.remove(profile.id)
        else:
            blog.likes.append(profile.id)
        blog.save()
        return HttpResponse(
            json.dumps({
                'likes': len(blog.likes)
            }),
            content_type='application/json'
            )