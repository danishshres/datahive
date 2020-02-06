from rest_framework import serializers
from .models import Job, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'created', 'attributes',)


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('project', 'filename', 'regions', 'file_attributes',)

class CurrentJobSerializer(serializers.Serializer):
    job = JobSerializer()
    project = ProjectSerializer()

    # class Meta:
    #     model = Job
    #     fields = ('project', 'filename', 'regions', 'file_attributes',)
