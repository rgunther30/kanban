from django.shortcuts import render, HttpResponse, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from board.models import Task, AddTaskForm, AddCommentForm

@login_required
def AboutView(request):
    return render(request, 'board/about.html')

def LogoutView(request):
    logout(request)
    return render(request, 'board/logout.html')

@login_required
def IndexView(request):
    current_user = request.user
    titles = ["To do", "In Progress", "Finished"]
    tasks = [Task.objects.filter(creator=current_user, state=search_state) for search_state in titles]
    titles_and_tasks = zip(titles, tasks)
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
            return redirect("board:index")
        else:
            print "Not Valid."
    else:
        form = AddTaskForm()
    return render(request, 'board/addtask.html', {'form': form})

@login_required
def EditTaskView(request):
    if request.method == 'POST':
        try:
            task_id = request.POST.get('task_id')
            task = Task.objects.get(id=task_id)
            if 'progress' in request.POST:
                advance_progress(task)
            elif 'regress' in request.POST:
                revert_progress(task)
            elif 'delete' in request.POST:
                task.delete()
            elif 'view_task' in request.POST:
                task_page = "board:task/" 
                print task_page
                return redirect(task_page, task_id)
            elif 'add_comment' in request.POST:
                return redirect("board:addcomment")
        except Exception, e:
            print "Error! " + str(e)
    return redirect('board:index')

@login_required
def AddCommentView(request):
    if request.method == 'POST':
        comment_form = AddCommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
        else:
            print "Not Valid."
    else:
        comment_form = AddCommentForm()
    return render(request, 'board/addtask.html', {'form': comment_form})

@login_required
def TaskView(request, key):
    task = Task.objects.get(pk=key)
    return render(request, 'board/taskview.html', { 'task': task })

def advance_progress(task):
    if task.state == 'To do':
        task.state = 'In Progress'
    elif task.state == 'In Progress':
        task.state = 'Finished'
    task.save()

def revert_progress(task):
    if task.state == 'In Progress':
        task.state = 'To do'
    elif task.state == 'Finished':
        task.state = 'In Progress'
    task.save()