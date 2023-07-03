from django.contrib.auth.models import AbstractUser
from django.db import models
# from oauth2_provider.models import AbstractApplication


class EndUser(AbstractUser):
    pass
    nickname = models.CharField(max_length=50, null=True, default="Harry")
    

    def __str__(self):
        return self.username




# class OAuthApplication(AbstractApplication):
#     # name: The name of the OAuth application.
#     # client_id: The client identifier of the application.
#     # client_secret: The client secret of the application.
#     # user:The user associated with the application.
    
#     pass

