from django.contrib import admin
from board.models import User, Todo, InProgress, Finished

class TodoInline(admin.StackedInline):
    model = Todo
    extra = 3

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['userid']}),
        ('Date Information', {'fields': ['email'], 'classes': ['collapse']}),
    ]
    inlines = [TodoInline]

admin.site.register(User, UserAdmin)
admin.site.register(Todo)
admin.site.register(InProgress)
admin.site.register(Finished)