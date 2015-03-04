from django.contrib import admin
from django.contrib.auth.models import User
from board.models import Task

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tasks', {'fields': ['creator', 'owner', 'name', 'description', 'state', 'work_date', 'finished_date']})
    ]

admin.site.register(Task, TaskAdmin)