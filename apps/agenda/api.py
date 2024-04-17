"""
    Script to generate all logic to Group and User serializer models.
"""
# Rest Framework
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# filters
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter

# Django
from django.shortcuts import get_object_or_404

# Models
from .models import Agenda

# Serializers
from .serializers import AgendaModelSerializer

class AgendaViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Agenda.objects.all()
    serializer_class = AgendaModelSerializer
    filter_backends  = [SearchFilter, OrderingFilter]
    search_fields  = ['contact_name', 'contact_last_name',]
    ordering_fields  = ['name', 'contact_last_name',]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Agenda.objects.all().filter(
            contact_assign=user).exclude(is_active=False)

    def list(self, request):
        """
            Function to list data of agenda object.
        """
        queryset = self.get_queryset()
        serializer = AgendaModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        """
            Function to create new agenda object.
        """
        serializer = AgendaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(contact_assign=request.user, is_active=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, pk=None):
        """
            Function to retrive data of agenda object.
        """
        queryset = self.get_queryset()
        agenda = get_object_or_404(queryset, pk=pk)
        serializer  = AgendaModelSerializer(agenda)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        """
            Function to update data of agenda object.
        """
        queryset = self.get_queryset()
        agenda  = get_object_or_404(queryset, pk=pk)
        if agenda.is_active is False:
            message = "Can't update this contact."
        else:
            serializer = AgendaModelSerializer(agenda, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            message = 'An error occurred'
        return Response({'data': message}, status=status.HTTP_304_NOT_MODIFIED)

    def partial_update(self, request, pk=None):
        """
            Function to partial update data of agenda object.
        """
        queryset = self.get_queryset()
        agenda  = get_object_or_404(queryset, pk=pk)
        if agenda.is_active is False:
            message = "Can't update this contact."
        else:
            serializer = AgendaModelSerializer(agenda, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            message = 'An error occurred'
        return Response({'data': message}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        agenda = get_object_or_404(queryset, pk=pk)
        if agenda:
            agenda.is_active = False
            agenda.save()
            message = 'Contact deleted'
            return Response({'data': message}, status=status.HTTP_200_OK)
        message = "Not data found"
        return Response({'data': message}, status=status.HTTP_404_NOT_FOUND)
