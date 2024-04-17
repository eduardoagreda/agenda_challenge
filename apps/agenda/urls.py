"""
    Scritp to generate all enpoint.
"""
from django.urls import path, include

from rest_framework import routers

# Views
from apps.users.api import UserViewSet, GroupViewSet
from .api import AgendaViewSet

router = routers.DefaultRouter()
router.register(r'agendas', AgendaViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
     path('', include(router.urls)),
]
