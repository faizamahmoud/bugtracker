from django.contrib.auth.models import AbstractUser
from django.db import models
from oauth2_provider.models import AbstractApplication
from bug.models import Bug, Project

class EndUser(AbstractUser):
    
    # user_permissions = models.ManyToManyField('auth.Permission', related_name='end_users')

    # bugs = models.ManyToManyField(Bug, related_name='users_bug')
    # projects = models.ManyToManyField(Project, related_name='users_projects')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='end_users')
    projects = models.ManyToManyField(Project, related_name='users', blank=True)
    bugs = models.ManyToManyField(Bug, related_name='users_bug', blank=True)


    def __str__(self):
        return self.username
    

    def __str__(self):
        return self.username
    

    
class OAuthApplication(AbstractApplication):
    # name: The name of the OAuth application.
    # client_id: The client identifier of the application.
    # client_secret: The client secret of the application.
    # user: The user associated with the application.
    
    pass

