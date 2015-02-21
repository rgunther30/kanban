from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from board.models import Todo, InProgress

# Create your views here.
def index(request):
    latest_todo_list = Todo.objects.order_by('-pub_date')[:5]
    context = { 'latest_todo_list': latest_todo_list}
    return render(request, 'board/index.html', context)

def TodoView(request, Todo_id):
    return HttpResponse(Todo.objects.get(id=Todo_id))

def InProgressView(request, InProgress_id):
    inprog = get_object_or_404(InProgress, pk=InProgress_id)
    return render(request, 'board/InProgress.html',  {'inprog': inprog })

def FinishedView(request, Finished_id):
    response = ("You've finished the task: %s" % Finished_id)
    return HttpResponse(response % Finished_id)

