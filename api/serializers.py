from rest_framework import serializers
from .models import Job, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'created', 'attributes',)


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        # fields = ('id', 'project', 'filename', 'regions', 'region_attributes', 'file_attributes',)
        fields = ('id', 'filename', 'regions', 'file_attributes',)
    
    def update(self, instance, validated_data, user_id):
        instance.file_attributes = validated_data.get('file_attributes', validated_data['file_attributes'])
        instance.regions = validated_data.get('regions', validated_data['regions'])
        instance.labeller_id = user_id
        instance.save()
        return instance


class CurrentJobSerializer(serializers.Serializer):
    job = JobSerializer()
    project = ProjectSerializer()

    # class Meta:
    #     model = Job
    #     fields = ('project', 'filename', 'regions', 'file_attributes',)
