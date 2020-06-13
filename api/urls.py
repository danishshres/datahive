from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.JobList.as_view()),
    path('jobs/<int:pk>/', views.JobDetail.as_view()),
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    # path('job/', views.CurrentJob.as_view()),
    path('job/', views.current_job),
    # path('login/  ', auth_views.login)
    # path('login/', auth_views.login, name='login', 
        # kwargs={'redirect_authenticated_user': True})
]