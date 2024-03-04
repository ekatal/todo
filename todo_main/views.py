from django.shortcuts import render
from todo.models import Task


def home(request):
	tasks = Task.objects.filter(is_completed=False).order_by('-updated')
	completed = Task.objects.filter(is_completed=True).order_by('-updated')
	context = {
		'tasks': tasks,
		'completed': completed,
	}
	return render(request, 'home.html', context)


def example(request):
	return render(request, 'example.html')
