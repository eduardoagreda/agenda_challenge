"""
    Script to generate a custom user model.
"""
from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.hashers import make_password

from .managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
        Custom user class that extends of AbstractBaseUser and PermissionsMixin
        to create a new custom user and add permissions aroud of the project.
        
        The Email field is unique form to access the data.
    """
    email = models.EmailField(_('Email address'), unique=True)
    first_name = models.CharField(_('First name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('Active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        """
            Metaclass to assign the verbose name and verbose name plural.
        """
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self) -> str:
        """
            Returns the first_name plus the last_name, with a space in between.
        """
        return f'{self.first_name}  {self.last_name}'.strip()

    def get_short_name(self) -> str:
        """
            Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
            Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
