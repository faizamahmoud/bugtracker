from django.urls import path
from . import views

app_name = 'bug'

urlpatterns = [
    # path('projects/', views.ProjectListView.as_view(), name='project_list'),
    # path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    # path('projects/create/', views.ProjectCreateView.as_view(), name='project_create'),
    # path('projects/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project_update'), # permissions for creator only     
    # path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'), # permissions for creator only     
    # path('bugs/', views.BugListView.as_view(), name='bug_list'),
    # path('bugs/<int:pk>/', views.BugDetailView.as_view(), name='bug_detail'), # bugs created by owner or in progress
    # path('bugs/create/', views.BugCreateView.as_view(), name='bug_create'),
    # path('bugs/<int:pk>/update/', views.BugUpdateView.as_view(), name='bug_update'),
    # path('bugs/<int:pk>/delete/', views.BugDeleteView.as_view(), name='bug_delete'),
]
