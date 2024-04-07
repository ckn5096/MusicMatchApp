from django.test import TestCase
from django.contrib.auth.models import User
from ..serializers import RegistrationSerializer


class RegistrationSerializerTest(TestCase):
    def test_registration_serializer_valid(self):
        data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com', 'username': 'johndoe', 'password': 'password123'}
        serializer = RegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_registration_serializer_invalid(self):
        data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com', 'username': 'johndoe'}  # Missing 'password'
        serializer = RegistrationSerializer(data=data)
        self.assertFalse(serializer.is_valid())
