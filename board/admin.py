from django.contrib import admin
from board.models import User, Task

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tasks', {'fields': ['creator', 'owner', 'name', 'description', 'state', 'work_date', 'finished_date']})
    ]

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['userid']}),
        ('Contact Information', {'fields': ['email', 'join_date']}),
    ]
    list_display = ('userid', 'email', 'join_date')
    list_filter = ['join_date']
    search_fields = ['userid']

admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)