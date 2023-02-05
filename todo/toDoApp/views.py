from django.shortcuts import render
from django.http import HttpResponseRedirect
from toDoApp.models import Task
from django.urls import reverse

def index(req):
    return render(req, 'index.html', {'tasks': Task.objects.all()})



def new_task(req):
    name = req.POST.get('name')
    desc = req.POST.get('description')
    is_done = False
    task = Task(name=name, description=desc, is_done=is_done)
    task.save()
    return HttpResponseRedirect(reverse('Home'))



def switch(req, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse('Home'))


def rem_task(req, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('Home'))
