from django.contrib import admin

# Register your models here.
from .models import Project, Job, ProjectUser

admin.site.register(Project)
admin.site.register(Job)
admin.site.register(ProjectUser)
