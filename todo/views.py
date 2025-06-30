from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task
# Create your views here.

def AddTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def completedtask(request):
    completedtask = Task.objects.filter(is_completed=True)
    context = {
        'completedtask':completedtask
    }
    return render(request,'home.html',context)

def updatetask(request):
    # is_completed = Task.object.get(task='')
    return HttpResponse('from update views')