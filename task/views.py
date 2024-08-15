from django.shortcuts import render,redirect
from task.forms import add_task
from task.models import TaskModel
# Create your views here.

def add_task_view(request):
    if request.method == 'POST':
        form = add_task(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = add_task()
    return render(request, 'add_task.html',{'form':form})


def edit_task(request,id):
    task=TaskModel.objects.get(pk=id)
    form = add_task(instance=task)
    if request.method == 'POST':
        form = add_task(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'add_task.html', {'form': form})


def delete_task(request,id):
    task=TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('home')