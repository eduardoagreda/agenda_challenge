"""
    Script to generate the serlializers of Agenda Model.
"""
from rest_framework.serializers import ModelSerializer

from .models import Agenda

class AgendaModelSerializer(ModelSerializer):
    """
        Class that extends of ModelSerializer to serialize Agenda Model.
    """
    class Meta:
        """
            Meta class that use the Agenda model to serializer.
        """
        model = Agenda
        fields = ['contact_name', 'contact_last_name', 'contact_phone_number', 'contact_email']
