"""
    Script to generare base model to extends a news models to create.
"""
from django.db.models import Model
from django.db.models import BooleanField
from django.db.models import DateTimeField

class BaseModel(Model):
    """ Base model from all models to implements in this project. """
    is_active = BooleanField('Flag to implement logical deletion', default=True)
    created_at = DateTimeField('Date and time of object created', auto_now_add=True)
    updated_at = DateTimeField('Date and time of object updated', auto_now=True)

    class Meta:
        """
            Metaclass to tell Django that this is an abstract model.
        """
        abstract = True
