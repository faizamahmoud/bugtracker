# In users/admin.py
from django.contrib import admin

from .models import Bug, Project, BugComment, ProjectComment, Profile

admin.site.register(Project)
admin.site.register(Bug)
admin.site.register(BugComment)
admin.site.register(ProjectComment)
admin.site.register(Profile)
