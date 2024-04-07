from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class RegistrationViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_registration_view(self):
        url = reverse('registration')
        data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com', 'username': 'johndoe', 'password': 'password123'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
<<<<<<< HEAD
        # Add more assertions as needed
=======

>>>>>>> origin/master


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_login_view(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'password123'}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
<<<<<<< HEAD
        # Add more assertions as needed
=======

>>>>>>> origin/master
