from django.contrib import admin
from .models import Project

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','project_current_state']

    def project_current_state(self,project):
        if project.project_state:
            return "Completed"
        return "Ongoing"