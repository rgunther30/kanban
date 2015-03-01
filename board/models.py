import datetime
from django.db import models
from django.utils import timezone

class User(models.Model):
    userid = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    join_date = models.DateTimeField('date joined')

    def __unicode__(self):
        return self.userid

class Task(models.Model):
    creator = models.ForeignKey('User', related_name='Creator')
    owner = models.ForeignKey('User', related_name='Owner')
    creation_date = models.DateTimeField('Date created', auto_now=True)
    work_date = models.DateTimeField('Initated date', blank=True, null=True)
    finished_date = models.DateTimeField('Date finished', blank=True, null=True)
    description = models.TextField(max_length=500)
    name = models.CharField(max_length=40)
    todo = 'todo'
    inprogress = 'inprogress'
    finished = 'finished'
    state_choices = (
        (todo, 'todo'),
        (inprogress, 'inprogress'),
        (finished, 'finished'),
        )
    state = models.CharField(max_length=12, choices=state_choices, default=todo)

    def __unicode__(self):
        return self.description

