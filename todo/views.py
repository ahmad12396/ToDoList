from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addtask (request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done (request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.iscompleted = True
    task.save()
    return redirect('home')

def mark_as_undone (request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.iscompleted = False
    task.save()
    return redirect('home')

def delete (request , pk):
    delete_task = get_object_or_404(Task , pk=pk)
    delete_task.delete()
    return redirect('home')

def updated (request , pk):
    get_task = get_object_or_404(Task , pk=pk)

    if request.method == 'POST':
        update_task = request.POST['task']
        get_task.task = update_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task' : get_task,
        }
        return render(request , 'edit.html', context)

def delete_completed_task (request , pk):
    delete_completed_task = get_object_or_404(Task , pk=pk)
    delete_completed_task.iscompleted = True
    delete_completed_task.delete()
    return redirect('home')