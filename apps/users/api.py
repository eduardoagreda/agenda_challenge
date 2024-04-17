"""
    Script to generate all logic to Group and User serializer models.
"""
from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets

# filters
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter


from .models import CustomUser
from .serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends  = [SearchFilter, OrderingFilter]
    search_fields  = ['first_name',]
    ordering_fields  = ['first_name',]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    filter_backends  = [SearchFilter, OrderingFilter]
    search_fields  = ['name',]
    ordering_fields  = ['name',]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
