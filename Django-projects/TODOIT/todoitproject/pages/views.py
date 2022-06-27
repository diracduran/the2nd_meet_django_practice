from django.shortcuts import render, redirect
from tasks.models import Task 
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required 
def index(request): 
    tasks = Task.objects.all().filter(user=request.user) 
    context = { 
        'tasks': tasks, 
    } 
    return render(request, 'pages/index.html', context=context)

@login_required 
def create_task(request): 
    if request.method == 'POST': 
        new_task = Task() 
        if 'title' in request.POST: 
            new_task.title = request.POST['title'] 
        if 'description' in request.POST: 
            new_task.description = request.POST['description'] 
        if 'priority' in request.POST: 
            new_task.priority = request.POST['priority'] 
        new_task.save() 
        messages.success(request, f'Task #{new_task.id} successfully created!') 
        return redirect('index')

@login_required 
def complete_task(request, task_id): 
    task = Task.objects.get(id=task_id) 
    task.is_completed = not task.is_completed 
    task.save() 
    messages.success(request, f'Task #{task.id} successfully completed!') 
    return redirect('index')

@login_required 
def complete_all_tasks(request): 
    tasks = Task.objects.filter(is_completed=False) 
    for task in tasks: 
        task.is_completed = True 
        task.save() 
    messages.success(request, 'All Tasks successfully completed!') 
    return redirect('index')

@login_required 
def delete_task(request, task_id): 
    task = Task.objects.get(id=task_id) 
    task.delete() 
    messages.warning(request, f'Task #{task.id} successfully deleted!') 
    return redirect('index')

@login_required 
def delete_active_tasks(request): 
    tasks = Task.objects.all() 
    for task in tasks: 
        if task.is_completed == False:
            task.delete() 
    messages.warning(request, 'All Active tasks successfully deleted!') 
    return redirect('index')

@login_required 
def delete_completed_tasks(request): 
    tasks = Task.objects.all() 
    for task in tasks: 
        if task.is_completed == True:
            task.delete()  
    messages.warning(request, 'All Completed tasks successfully deleted!') 
    return redirect('index')

@login_required 
def edit(request, task_id): 
    task = Task.objects.get(id=task_id) 
    context = { 
        'task': task, 
    } 
    if request.method == 'GET': 
        return render(request, 'pages/edit.html', context=context)    
    if request.method == 'POST': 
        if 'title' in request.POST: 
            task.title = request.POST['title'] 
        if 'description' in request.POST: 
            task.description = request.POST['description'] 
        if 'priority' in request.POST: 
            task.priority = request.POST['priority'] 
        task.save() 
        messages.success(request, f'Task #{task.id} successfully updated!') 
        return redirect('index')

@login_required 
def profile(request): 
    tasks = Task.objects.filter(user=request.user) 
    context = { 
        'active_tasks': tasks.filter(is_completed=False).count(), 
        'completed_tasks': tasks.filter(is_completed=True).count(), 
    } 
    return render(request, 'pages/profile.html', context=context)