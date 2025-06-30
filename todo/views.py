from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task
# Create your views here.

def AddTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request,pk):
    completed_task = get_object_or_404(Task,pk=pk)
    completed_task.is_completed = True
    completed_task.save()
    return redirect('home')

def mark_as_undo(request,pk):
    undo_task = get_object_or_404(Task,pk=pk)
    undo_task.is_completed = False
    undo_task.save()
    return redirect('home')
    # return HttpResponse('from mark_as_undo')