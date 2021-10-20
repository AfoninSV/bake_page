from django.shortcuts import render, redirect, get_object_or_404
from .models import Example

def ex_list(request):
	queryset = Example.objects.all()
	context = {
		'object_list' : queryset
	}
	return render(request, 'base.html', context)
