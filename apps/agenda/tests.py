"""
    Script to generate test case of Agenda model.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.agenda.models import Agenda


class AgendaTestCase(TestCase):
    """
        Agenda model test case.
    """

    def setUp(self):
        """
            Function setup to create an Agenda object.
        """
        self.new_user = get_user_model().objects.create(
            first_name = 'Eduardo',
            last_name = 'Agreda',
            email = 'eagreda@gmail.com'
        )

        self.new_agenda = Agenda.objects.create(
            contact_name='Eduardo',
            contact_last_name='Agreda Lopez',
            contact_phone_number='9612332565',
            contact_email = 'eduardoagreda25@gmail.com',
            contact_assign = self.new_user
        )


    def test_string_representation(self):
        """
            Test case to verify that the representation name of
            the agenda object generated in the setup function is equal
            to the magic function __str__ in the Agenda model.
        """
        self.assertEqual(str(self.new_agenda),
                         f'{self.new_agenda.contact_name} {self.new_agenda.contact_last_name}')


    def test_confirm_agenda_creation(self):
        """
            Test case to verify that the agenda object generated in the
            setup function is true.
        """
        self.assertEqual(self.new_agenda.is_active, True)
