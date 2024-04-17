"""
    Script to register a model into django admin.
"""
from django.contrib import admin

from .models import CustomUser

# Register your models here.
admin.site.register(CustomUser)