from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_description = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')

class InProgress(models.Model):
    description = models.CharField(max_length=400)
    date_started = models.DateTimeField('date started')

class Finished(models.Model):
    finished_description = models.CharField(max_length=400)
    date_started = models.DateTimeField('date finished')

