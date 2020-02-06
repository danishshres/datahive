from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('jobs/', views.JobList.as_view()),
    path('jobs/<int:pk>/', views.JobDetail.as_view()),
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('job/', views.CurrentJob.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)