# In users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EndUser

class CustomUserAdmin(UserAdmin):
    model = EndUser

admin.site.register(EndUser, CustomUserAdmin)