
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('api/', include('bug.urls')),
    path("", include('user.urls')),
]
