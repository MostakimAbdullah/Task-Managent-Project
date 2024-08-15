from django.db import models
from category.models import TaskCategory
# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_Assign_Date = models.DateTimeField(auto_now_add=True)
    category=models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.taskTitle