from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Task
from .forms import TaskForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    username = 'default'
    if request.user.is_authenticated:
        username = request.user.username
        
    # if request.method == "POST":
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         task = form.cleaned_data['task']
    #         description = form.cleaned_data['description']
    #         form.save()
    #     else:
    #         print('error')
    
    # form = TaskForm()
    tasks = Task.objects.filter(author=username)
    all_tasks = []

    done_tasks = 0
    for task in tasks:
        task_info = {
            'id': task.id,
            'task': task.task,
            'description': task.description,
            'done': task.done,
            'date': task.date,
            'author': task.author
        }
        if task.done == True:
            done_tasks += 1
        all_tasks.append(task_info)
    all_tasks.reverse()
    count_tasks = len(all_tasks)
    context = {'all_tasks': all_tasks, 'count_tasks': count_tasks, 'done_tasks': done_tasks, 'username': username}

    return render(request, 'todo/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='/accounts/login/')
def add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            description = form.cleaned_data['description']
            form.save()
            return redirect('home')
        else:
            print('error')
    
    form = TaskForm()
    context = {'form': form}
    return render(request, 'todo/add.html', context)

def done(request, id):
    username = 'default'
    if request.user.is_authenticated:
        username = request.user.username
    try:
        task = Task.objects.get(id=id)
        if task.author == username:
            task.done = True
            task.save()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Произошла ошибка!</h2>")

def undo(request, id):
    username = 'default'
    if request.user.is_authenticated:
        username = request.user.username
    try:
        task = Task.objects.get(id=id)
        if task.author == username:
            task.done = False
            task.save()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Произошла ошибка!</h2>")

@login_required(login_url='/accounts/login/')
def delete(request, id):
    username = 'default'
    if request.user.is_authenticated:
        username = request.user.username
    try:
        task = Task.objects.get(id=id)
        if task.author == username or username == 'admin':
            task.delete()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Произошла ошибка!</h2>")
