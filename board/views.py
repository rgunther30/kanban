from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic

from board.models import Task

def IndexView(request):
    todo = Task.objects.filter(state='todo')
    inprogress = Task.objects.filter(state='inprogress')
    finished = Task.objects.filter(state='finished')
    return render(request, 'board/index.html', { 'todo': todo, 'inprogress': inprogress, 'finished': finished })

def TaskView(request, key):
    task = Task.objects.get(pk=key)
    return render(request, 'board/taskview.html', { 'task': task })