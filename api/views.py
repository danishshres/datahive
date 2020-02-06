from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Job, Project, ProjectUser
from .serializers import JobSerializer, ProjectSerializer, CurrentJobSerializer
from .permissions import IsAdminOrEditOnly, IsAdminUser
from rest_framework.permissions import DjangoModelPermissions

#Admin
class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsAdminOrEditOnly, DjangoModelPermissions)

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsAdminOrEditOnly, DjangoModelPermissions)

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAdminUser)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAdminUser)

#Labellar
class CurrentJob(generics.RetrieveAPIView):
    # queryset = Job.objects.all()
    serializer_class = CurrentJobSerializer

    def retrieve(self, request, *args, **kwargs):
        user = self.request.user
        projectuser = ProjectUser.objects.get(user_id=self.request.user.id)
        # project = Project.objects.get(pk=projectuser.project_id)
        job = Job.objects.get(project_id=projectuser.project_id)
        serializer = self.get_serializer({'job':job, 'project':job.project})
        return Response(serializer.data)
