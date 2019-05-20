from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Task
from .forms import TaskForm

def index(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            description = form.cleaned_data['description']
            form.save()
    
    form = TaskForm()

    tasks = Task.objects.all()
    all_tasks = []

    done_tasks = 0
    for task in tasks:
        task_info = {
            'id': task.id,
            'task': task.task,
            'description': task.description,
            'done': task.done,
            'date': task.date
        }
        if task.done == True:
            done_tasks += 1
        all_tasks.append(task_info)
    all_tasks.reverse()
    count_tasks = len(all_tasks)
    context = {'all_tasks': all_tasks, 'count_tasks': count_tasks, 'done_tasks': done_tasks}

    return render(request, 'todo/index.html', context)

def add(request):
    form = TaskForm()
    context = {'form': form}
    return render(request, 'todo/add.html', context)

def done(request, id):
    try:
        task = Task.objects.get(id=id)
        task.done = True
        task.save()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Произошла ошибка!</h2>")

def undo(request, id):
    try:
        task = Task.objects.get(id=id)
        task.done = False
        task.save()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Произошла ошибка!</h2>")

def delete(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return HttpResponseRedirect("/")
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Произошла ошибка!</h2>")
