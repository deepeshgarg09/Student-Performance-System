from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model

class StudentViewTest(TestCase):

    def setUp(self):
        self.student = get_user_model().objects.create_user(
            username='testuser',
            password='pass1234',
            roll_number='12345',
            department='Computer Science'
        )
        self.client.login(username='testuser', password='pass1234')
        
    @override_settings(CACHES={
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    })
    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'performance/dashboard.html')

    def test_login_view(self):
        self.client.logout()
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'pass1234'
        })
        self.assertEqual(response.status_code, 302) 

    def test_registration_view(self):
        self.client.logout()
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpass1234',
            'password2': 'newpass1234',
            'roll_number': '54321',
            'department': 'Physics'
        })
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())

