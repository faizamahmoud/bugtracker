from django.urls import path
from . import views

app_name = 'bug'

urlpatterns = [
    # path('front/', views.front, name='front'),
    path('', views.project_list, name='project_list'), #/api
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:pk>/update/', views.project_update, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('bug/', views.bug_list, name='bug_list'),
    path('bug/<int:pk>/', views.bug_detail, name='bug_detail'),
    path('bug/create/', views.bug_create, name='bug_create'),
    path('bug/<int:pk>/update/', views.bug_update, name='bug_update'),
    path('bug/<int:pk>/delete/', views.bug_delete, name='bug_delete'),
]
