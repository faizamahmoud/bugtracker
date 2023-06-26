from django.contrib.auth.models import AbstractUser
from django.db import models
from oauth2_provider.models import AbstractApplication
from bug.models import Bug, Project

class EndUser(AbstractUser):
    groups = models.ManyToManyField('auth.Group', related_name='end_users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='end_users')

    bugs = models.ManyToManyField(Bug, related_name='users_bug')
    projects = models.ManyToManyField(Project, related_name='users_projects')

    def __str__(self):
        return self.username
    
    
class OAuthApplication(AbstractApplication):
    # name: The name of the OAuth application.
    # client_id: The client identifier of the application.
    # client_secret: The client secret of the application.
    # user: The user associated with the application.
    
    pass

