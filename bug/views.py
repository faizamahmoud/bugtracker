from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Project, Bug
from .serializers import ProjectSerializer, BugSerializer


# Project Views
@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)

@api_view(['POST'])
def project_create(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    serializer = ProjectSerializer(project, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Bug Views
@api_view(['GET'])
def bug_list(request):
    bugs = Bug.objects.all()
    serializer = BugSerializer(bugs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bug_detail(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    serializer = BugSerializer(bug)
    return Response(serializer.data)

@api_view(['POST'])
def bug_create(request):
    serializer = BugSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def bug_update(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    serializer = BugSerializer(bug, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def bug_delete(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    bug.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
