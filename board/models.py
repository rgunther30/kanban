import datetime
from django.db import models
from django.utils import timezone

class User(models.Model):
    userid = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    join_date = models.DateTimeField('date joined')

class Todo(models.Model):
    todo_description = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, related_name='todo_user', null=True, blank=True)

    def __unicode__(self):
        return self.todo_description

    def recently_published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class InProgress(models.Model):
    description = models.CharField(max_length=400)
    date_started = models.DateTimeField('date started')
    user = models.ForeignKey('User', related_name='inprogress_user', null=True, blank=True)

    def __unicode__(self):
        return self.description

class Finished(models.Model):
    finished_description = models.CharField(max_length=400)
    date_started = models.DateTimeField('date finished')
    user = models.ForeignKey('User', related_name='finished_user', null=True, blank=True)

    def __unicode__(self):
        return self.finished_description


