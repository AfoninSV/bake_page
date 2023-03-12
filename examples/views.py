from django.shortcuts import render, redirect, get_object_or_404
from .models import Example
from .forms import InputForm


# Get! Shows items list
def ex_list(request):
    queryset = Example.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'base.html', context)


# POST! Create a Card
def ex_create(request):
    if request.method == 'POST':
        form = InputForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data.get('title'))
        context = {
            'form': form
        }
        return render(request,"create.html", context)
