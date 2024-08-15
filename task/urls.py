from django.urls import path
from . import views
urlpatterns =[
    path('add/', views.add_task_view, name='add_task'),
    path('edit/<int:id>', views.edit_task, name='edit'),
    path('delete/<int:id>', views.delete_task, name='delete'),
]