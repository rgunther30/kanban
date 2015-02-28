from django.contrib import admin
from board.models import User, Todo, InProgress, Finished

class TodoInline(admin.StackedInline):
    model = Todo
    extra = 3

class InProgressAdmin(admin.ModelAdmin):
    fieldsets = [
        ('In Progress', {'fields': ['description', 'date_started', 'user']})
    ]

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['userid']}),
        ('Contact Information', {'fields': ['email', 'join_date']}),
    ]
    inlines = [TodoInline]
    list_display = ('userid', 'email', 'join_date')
    list_filter = ['join_date']
    search_fields = ['userid']



admin.site.register(User, UserAdmin)
admin.site.register(Todo)
admin.site.register(InProgress)
admin.site.register(Finished)