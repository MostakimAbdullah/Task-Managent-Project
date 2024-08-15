from django.shortcuts import render
from task.models import TaskModel

def index(request):
    data=TaskModel.objects.all()
    return render(request, 'base.html', {'data':data})