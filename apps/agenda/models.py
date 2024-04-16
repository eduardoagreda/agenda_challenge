"""
    Script to generate Agenda model.
"""
from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model


class Agenda(models.Model):
    """
        Class to create Agenda model.
    """
    public_id: str = models.CharField(
        max_length=36,
        null=False,
        blank=False,
        db_index=True)
    contact_name: str = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        db_index=True
    )
    contact_lastname: str = models.CharField(
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
        get_user_model(),
        on_delete=models.CASCADE
    )
    is_active: bool = models.BooleanField(
        default=True
    )
    created_at: str = models.DateTimeField(auto_now_add=True)
    updated_at: str = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.public_id = uuid4()
        super(Agenda, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.contact_name} {self.contact_lastname}'

    def get_full_name(self) -> str:
        """
            Return full name of contact.
        """
        return str(self.contact_name + self.contact_lastname)

    class Meta:
        verbose_name = 'agenda'
        verbose_name_plural = 'agendas'
        ordering = ['contact_lastname']
