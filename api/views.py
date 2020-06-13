from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Job, Project, ProjectUser
from .serializers import JobSerializer, ProjectSerializer, CurrentJobSerializer
from .permissions import IsAdminOrEditOnly, IsAdminUser
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import views, status
from rest_framework.decorators import api_view

from django.contrib.auth.decorators import login_required


#Admin
# @login_required
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
    permission_classes = (IsAdminOrEditOnly, DjangoModelPermissions)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAdminOrEditOnly, DjangoModelPermissions)


from django.http import Http404
#Labellar
class CurrentJob(generics.RetrieveAPIView):
    """
        -assign a job to the user
        -send back the job that is assigned.
    """
    # queryset = Job.objects.all()
    serializer_class = CurrentJobSerializer
    # permission_classes = (IsAdminOrEditOnly, DjangoModelPermissions)
    # def get(self):
    def retrieve(self, request, *args, **kwargs):
        user = self.request.user
        try:
            projectuser = ProjectUser.objects.get(user_id=self.request.user.id)
            project = Project.objects.get(id=projectuser.project_id)
            if project.status == 1:
                # job = Job.objects.get(project_id=project.id)
                job = Job.objects.filter(project_id=project.id, labeller_id=None)[0]
                serializer = self.get_serializer({'job':job, 'project':job.project})
        except:
            raise Http404("No project assigned !")
        return Response(serializer.data)
    # def retrieve(self, request, *args, **kwargs): 
        # user = self.request.user
        # projectuser = ProjectUser.objects.get(user_id=self.request.user.id)
        # # project = Project.objects.get(pk=projectuser.project_id)
        # job = Job.objects.get(project_id=projectuser.project_id)
        # serializer = self.get_serializer({'job':job, 'project':job.project})
        # return Response(serializer.data)

@api_view(['GET', 'POST'])
def current_job(request):
    if request.method == 'GET':
        serializer_class = CurrentJobSerializer
        user = request.user
        try:
            projectuser = ProjectUser.objects.get(user_id=request.user.id)
            project = Project.objects.get(id=projectuser.project_id)
            if project.status == 1:
                # job = Job.objects.get(project_id=project.id)
                job = Job.objects.filter(project_id=project.id, labeller_id=0).order_by('id')[0]
                serializer = CurrentJobSerializer({'job':job, 'project':job.project, 'labeller_id':request.user.id})
            return Response(serializer.data)
        except:
            raise Http404("No project assigned !")
    elif request.method == 'POST':
        current_job = Job.objects.filter(id=request.data['id'])[0]
        serializer = JobSerializer(current_job)
        # if serializer.is_valid():
        serializer.update(current_job, request.data, user_id=request.user.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

from django.http import HttpResponse
from django.template import loader
import os

@login_required(login_url='/api-auth/login/?next=/index')
def index(request):
    # html_file = open('src/index.html')

    template = loader.get_template('index.html')
    context = None
    return HttpResponse(template.render(context, request))
    # html = '<h +'</h1></html>'
    # return HttpResponse(html_file)
