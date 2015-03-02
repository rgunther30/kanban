from django.shortcuts import render, HttpResponse, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from board.models import Task

@login_required
def AboutView(request):
    return render(request, 'board/about.html')

def LoginView(request):
	return render(request, 'board/login.html')

@login_required
def IndexView(request):
    todo = Task.objects.filter(state='todo')
    inprogress = Task.objects.filter(state='inprogress')
    finished = Task.objects.filter(state='finished')
    return render(request, 'board/index.html', { 'todo': todo, 'inprogress': inprogress, 'finished': finished })

@login_required
def ProfileView(request):
	user = request.user
	return render(request, 'board/profile.html', {'user': user})

@login_required
def TaskView(request, key):
    task = Task.objects.get(pk=key)
    return render(request, 'board/taskview.html', { 'task': task })

