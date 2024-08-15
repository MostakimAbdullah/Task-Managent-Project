from django.shortcuts import render,redirect
from category.forms import Add_Category

# Create your views here.
def add_category_view(request):
    if request.method == 'POST':
        form = Add_Category(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = Add_Category()
    return render(request, 'add_category.html', {'form': form})
            