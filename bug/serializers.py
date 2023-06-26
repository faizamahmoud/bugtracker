from rest_framework import serializers
from .models import Project, Bug

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'due_date')
        
        
class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = ['number', 'issue_title', 'details', 'priority', 'steps_to_recreate', 'opened_on', 'date_resolved', 'time_tracker', 'status', 'project']

    
    
    
    


