from django import forms

from .models import Agenda

class AgendaForm(forms.ModelForm):

    class Meta:
        model = Agenda
        fields = ('contact_name', 'contact_lastname', 'contact_phone_number', 'contact_email')
