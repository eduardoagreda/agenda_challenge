"""
    Script to generate Agenda model.
"""
from django.db import models
from django.conf import settings

from utils.models import BaseModel


class Agenda(BaseModel):
    """
        Class to create Agenda model that extends from BaseModel utility.
    """
    contact_name: str = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        db_index=True
    )
    contact_last_name: str = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        db_index=True
    )
    contact_phone_number: str = models.CharField(
        max_length=10,
        null=False,
        blank=False
    )
    contact_email: str = models.EmailField(
        blank=True,
        null=True
    )
    contact_assign = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def get_full_name(self) -> str:
        """
            Return full name of contact.
        """
        return f'{self.contact_name} {self.contact_last_name}'

    def __str__(self) -> str:
        return self.get_full_name()

    class Meta:
        verbose_name = 'agenda'
        verbose_name_plural = 'agendas'
