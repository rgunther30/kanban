from django.shortcuts import render, HttpResponse, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from board.models import Task, AddTaskForm

@login_required
def AboutView(request):
    return render(request, 'board/about.html')

def LogoutView(request):
    logout(request)
    return render(request, 'board/logout.html')

@login_required
def IndexView(request):
    current_user = request.user
    todo = Task.objects.filter(creator=current_user, state='To do')
    inprogress = Task.objects.filter(creator=current_user, state='In Progress')
    finished = Task.objects.filter(creator=current_user, state='finished')
    tasks = [todo, inprogress, finished]
    titles = ["To do", "In Progress", "Finished"]
    titles_and_tasks = zip(titles, tasks)
    print titles_and_tasks
    return render(request, 'board/index.html', { 'titles_and_tasks': titles_and_tasks })

@login_required
def ProfileView(request):
	user = request.user
	return render(request, 'board/profile.html', {'user': user})

@login_required
def AddTaskView(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print "Not Valid."
    else:
        form = AddTaskForm()
    return render(request, 'board/addtask.html', {'form': form})

@login_required
def DeleteTaskView(request):
    if request.method == 'POST':
        try:
            task_id = request.POST.get('task_id')
            task = Task.objects.get(id=task_id)
            task.delete()
        except:
            print "Error!"
    return redirect('board:index')

@login_required
def TaskView(request, key):
    task = Task.objects.get(pk=key)
    return render(request, 'board/taskview.html', { 'task': task })

