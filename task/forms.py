from django import forms
from task.models import TaskModel


class add_task(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        labels = {
            'taskTitle': 'Task Title',
            'taskDescription': 'Task Description',
        }

