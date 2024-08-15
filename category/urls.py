from django.urls import path
from . import views

urlpatterns =[
    path('add/', views.add_category_view , name= 'add_category'),
]