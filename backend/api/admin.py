"""Панель администратора."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Вывод строк в панели администратора."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
