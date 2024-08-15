from django import forms
from category.models import TaskCategory

class Add_Category(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = '__all__'
        labels = {
            'category_name': 'Category Name',
        }