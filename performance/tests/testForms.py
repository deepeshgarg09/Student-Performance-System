from django.test import TestCase
from performance.forms import StudentRegistrationForm

class StudentRegistrationFormTest(TestCase):

    def test_valid_registration_form(self):
        form = StudentRegistrationForm(data={
            'username': 'testuser1',
            'roll_number': '12345',
            'department': 'Computer Science',
            'password1': 'pass1234pass',
            'password2': 'pass1234pass',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_registration_form(self):
        form = StudentRegistrationForm(data={
            'username': 'testuser',
            'password1': 'pass1234',
            'password2': 'differentpass',
            'roll_number': '12345',
            'department': 'Computer Science'
        })
        self.assertFalse(form.is_valid())

