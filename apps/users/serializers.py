"""
    Script to generate the serlializers of User Model.
"""
from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
        Class that extends of HyperlinkModelserializer to 
        obtain an URL across User model.
    """
    class Meta:
        """
            Meta class that use the User model to serialize some
            field how: url, username, email and groups.
        """
        model = CustomUser
        fields = ['url', 'first_name', 'password', 'last_name', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
        Class that extends of HyperlinkModelserializer to 
        obtain an URL across Group model.
    """
    class Meta:
        """
            Meta class that use the Group model to serialize some
            field how: url and name.
        """
        model = Group
        fields = ['url', 'name']
