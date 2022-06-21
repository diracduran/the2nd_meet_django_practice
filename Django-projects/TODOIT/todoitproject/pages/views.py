from django.shortcuts import render, redirect
from tasks.models import Task 
from django.contrib import messages

# Create your views here.
def index(request): 
    tasks = Task.objects.all() 
    context = { 
        'tasks': tasks, 
    } 
    return render(request, 'pages/index.html', context=context)

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

def complete_task(request, task_id): 
    task = Task.objects.get(id=task_id) 
    task.is_completed = not task.is_completed 
    task.save() 
    messages.success(request, f'Task #{task.id} successfully completed!') 
    return redirect('index')

def complete_all_tasks(request): 
    tasks = Task.objects.filter(is_completed=False) 
    for task in tasks: 
        task.is_completed = True 
        task.save() 
    messages.success(request, 'All Tasks successfully completed!') 
    return redirect('index')

def delete_task(request, task_id): 
    task = Task.objects.get(id=task_id) 
    task.delete() 
    messages.warning(request, f'Task #{task.id} successfully deleted!') 
    return redirect('index')

def delete_active_tasks(request): 
    tasks = Task.objects.all() 
    for task in tasks: 
        if task.is_completed == False:
            task.delete() 
    messages.warning(request, 'All Active tasks successfully deleted!') 
    return redirect('index')

def delete_completed_tasks(request): 
    tasks = Task.objects.all() 
    for task in tasks: 
        if task.is_completed == True:
            task.delete()  
    messages.warning(request, 'All Completed tasks successfully deleted!') 
    return redirect('index')

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

def login(request): 
    context = {} 
    return render(request, 'pages/login.html', context=context)

def profile(request): 
    context = {} 
    return render(request, 'pages/profile.html', context=context)

def register(request): 
    context = {} 
    return render(request, 'pages/register.html', context=context)