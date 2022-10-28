from django.contrib import admin
from projects.models import Project
from tasks.models import Task


@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "owner",
    )
