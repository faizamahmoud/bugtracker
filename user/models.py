from django.contrib.auth.models import AbstractUser
from django.db import models
# from oauth2_provider.models import AbstractApplication


class EndUser(AbstractUser):
    pass
    nickname = models.CharField(max_length=50, null=True, default="Harry")
    # user_permissions = models.ManyToManyField('auth.Permission', related_name='end_users')
    # managing_projects = models.ManyToManyField('bug.Project', related_name='users', blank=True)
    # bugs = models.ManyToManyField('bug.Bug', related_name='users_bug', blank=True)


    def __str__(self):
        return self.username




# class OAuthApplication(AbstractApplication):
#     # name: The name of the OAuth application.
#     # client_id: The client identifier of the application.
#     # client_secret: The client secret of the application.
#     # user:The user associated with the application.
    
#     pass

