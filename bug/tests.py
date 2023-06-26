from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Project, Bug
from .serializers import ProjectSerializer, BugSerializer

class ProjectBugAPITestCase(APITestCase):
    def setUp(self):
        self.project = Project.objects.create(name='Test Project', due_date='2023-01-01')
        self.bug = Bug.objects.create(
            issue_title='Test Bug',
            details='Bug details',
            priority='high',
            steps_to_recreate='Steps to recreate the bug',
            project=self.project
        )
        
    def test_project_list(self):
        url = reverse('bug:project_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_project_detail(self):
        url = reverse('bug:project_detail', args=[self.project.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = ProjectSerializer(self.project)
        self.assertEqual(response.data, serializer.data)

    def test_project_create(self):
        url = reverse('bug:project_create')
        data = {'name': 'New Project', 'due_date': '2023-12-31'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        project = Project.objects.get(name='New Project')
        serializer = ProjectSerializer(project)
        self.assertEqual(response.data, serializer.data)

    def test_project_update(self):
        url = reverse('bug:project_update', args=[self.project.pk])
        data = {'name': 'Updated Project', 'due_date': '2023-06-30'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_project = Project.objects.get(pk=self.project.pk)
        serializer = ProjectSerializer(updated_project)
        self.assertEqual(response.data, serializer.data)

    def test_project_delete(self):
        url = reverse('bug:project_delete', args=[self.project.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Project.objects.filter(pk=self.project.pk).exists())

    def test_bug_list(self):
        url = reverse('bug:bug_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        bugs = Bug.objects.all()
        serializer = BugSerializer(bugs, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_bug_detail(self):
        url = reverse('bug:bug_detail', args=[self.bug.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = BugSerializer(self.bug)
        self.assertEqual(response.data, serializer.data)

    def test_bug_create(self):
        url = reverse('bug:bug_create')
        data = {
            'issue_title': 'New Bug',
            'details': 'Bug details',
            'priority': 'medium',
            'steps_to_recreate': 'Steps to recreate the bug',
            'project': self.project.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        bug = Bug.objects.get(issue_title='New Bug')
        