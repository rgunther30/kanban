from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views import generic

from board.models import Task

def IndexView(request):
    return HttpResponse('index.html')


def TaskView(request, task_name):
    tasks = Task.objects.filter(name=task_name)
    return HttpResponse(tasks)