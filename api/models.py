from django.db import models
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

class Project(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=2000, blank=False)
    attributes = models.CharField(max_length=2000, blank=False)
    status = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created']
    def __str__(self):
        return self.name

class Job(models.Model):
    project = models.ForeignKey('api.Project', on_delete=models.CASCADE)
    labeller = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True)
    filename = models.CharField(max_length=1000, blank=False)
    regions = models.CharField(max_length=1000, blank=True)
    file_attributes = models.CharField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.filename

class ProjectUser(models.Model):
    project = models.ForeignKey('api.Project', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)