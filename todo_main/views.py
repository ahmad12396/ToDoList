from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(iscompleted = False).order_by('-updated_at')
    completedtasks = Task.objects.filter(iscompleted = True).order_by('-updated_at')
    
    context = {
        "tasks" : tasks ,
        "completedtask" : completedtasks
    }

    return render(request , 'home.html', context)