import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm

class Task(models.Model):
    creator = models.ForeignKey(User, related_name='Creator')
    owner = models.ForeignKey(User, related_name='Owner')
    creation_date = models.DateTimeField('Date created', auto_now=True)
    work_date = models.DateTimeField('Worked started', blank=True, null=True)
    finished_date = models.DateTimeField('Date finished', blank=True, null=True)
    description = models.TextField(max_length=500)
    name = models.CharField(max_length=40)
    todo = 'To do'
    inprogress = 'In Progress'
    finished = 'Finished'
    state_choices = (
        (todo, 'To do'),
        (inprogress, 'In progress'),
        (finished, 'Finished'),
        )
    state = models.CharField(max_length=12, choices=state_choices, default=todo)

    def __unicode__(self):
        return self.description

class Comment(models.Model):
    writer = models.ForeignKey(User, related_name='Writer')
    body = models.TextField(max_length = 500)
    creation_date = models.DateTimeField('Date Created', auto_now=True)
    task_id = models.IntegerField()

class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'state', 'creator', 'owner', 'work_date', 'finished_date')

class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
