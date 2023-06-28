from datetime import timezone
from django.db import models
from django.contrib.auth import get_user_model


class Project(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,null=True, default="")
    project_name = models.CharField(max_length=100)
    members = models.ManyToManyField(get_user_model(), related_name='projects')
    bugs = models.ManyToManyField('Bug', related_name='projects')
    comments = models.ManyToManyField(get_user_model(), through='ProjectComment', related_name='project_comments')
    
    def get_bugs(self):
        return self.bugs.all()

    def __str__(self):
        return self.name

class Bug(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    number = models.AutoField(primary_key=True)
    issue_title = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    steps_to_recreate = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True, default='-')
    date_resolved = models.DateField(blank=True, null=True, default='-')
    time_tracker = models.DurationField(blank=True, null=True, default='-')
    status = models.CharField(
        max_length=20,
        choices=[
            ('in_progress', 'In Progress'),
            ('not_started', 'Not Started'),
            ('closed', 'Closed'),
            ('paused', 'On Pause'),
        ],
        default='not_started',
    )
    
    primary_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='created_bugs')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    comments = models.ManyToManyField(get_user_model(), through='BugComment', related_name='bug_comments')
    secondary_owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_bugs')


    def can_edit_bug(self, user):
        if self.secondary_owner is None:
            return user == self.primary_owner
        else:
            return user == self.secondary_owner


    def __str__(self):
        return self.issue_title



class BugComment(models.Model):
    associated_bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk is None:  # Check if the comment is being created
            self.last_updated = self.created_on  # Set last_updated same as created_on
        else:  # Comment is being updated
            self.last_updated = timezone.now()  # Update last_updated with current timestamp
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Comment by {self.owner.username} on {self.created_on}, last updated on {self.last_updated}"

class ProjectComment(models.Model):
    associated_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk is None:  # Check if the comment is being created
            self.last_updated = self.created_on  # Set last_updated same as created_on
        else:  # Comment is being updated
            self.last_updated = timezone.now()  # Update last_updated with current timestamp
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Comment by {self.owner.username} on {self.created_on}, last updated on {self.last_updated}"