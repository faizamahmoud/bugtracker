from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField()
    # update after User app and migrate
    # members = models.ManyToManyField('User', related_name='projects')
    
    def get_bugs(self):
        return self.issues.all()

    def __str__(self):
        return self.name

class Bug(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    number = models.AutoField(primary_key=True)
    issue_title = models.CharField(max_length=100)
    details = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    steps_to_recreate = models.TextField()
    opened_on = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateField(blank=True, null=True)
    time_tracker = models.DurationField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('in_progress', 'In Progress'),
            ('not_started', 'Not Started'),
            ('closed', 'Closed'),
        ],
        default='not_started',
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')

    def __str__(self):
        return self.issue_title
