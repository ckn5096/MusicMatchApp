from django.test import TestCase
from ..models import CustomUser


class CustomUserModelTest(TestCase):
    def test_custom_user_creation(self):
        user = CustomUser.objects.create(username='testuser', password='password123')
        self.assertEqual(user.username, 'testuser')
<<<<<<< HEAD
        # Add more assertions as needed
=======

>>>>>>> origin/master
