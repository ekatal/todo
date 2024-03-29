from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
	list_display = ('task', 'is_completed', 'updated')


admin.site.register(Task, TaskAdmin)
