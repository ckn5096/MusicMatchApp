from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from ..models import MusicPreference, Playlist
from django.contrib.auth.models import User
import json
from rest_framework.authtoken.models import Token

class MusicPreferenceViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.token = Token.objects.create(user=self.user)

    def test_get_music_preference(self):
        url = reverse('MusicPreference')
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.assertEqual(response.status_code, 200)

    def test_post_music_preference(self):
        url = reverse('MusicPreference')
        music_preference_data = {
            'favorite_genre': 'Rock',
            'favorite_artist': 'Metallica',
            'favorite_song': 'Enter Sandman'
        }
        response = self.client.post(url, data=json.dumps(music_preference_data), content_type='application/json',
                                    HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.assertEqual(response.status_code, 201)


    # def test_get_music_preference(self):
    #     # Authenticate user
    #     self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
    #
    #     # Create music preference
    #     MusicPreference.objects.create(
    #         user=self.user,
    #         favorite_genre='Rock',
    #         favorite_artist='The Beatles',
    #         favorite_song='Hey Jude'
    #     )
    #
    #     # Get music preference
    #     response = self.client.get(reverse('MusicPreference'))
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['favorite_genre'], 'Rock')
    #
    # def test_post_music_preference(self):
    #     # Authenticate user
    #     self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
    #
    #     # Create music preference data
    #     music_preference_data = {'favorite_genre': 'Rock', 'favorite_artist': 'The Beatles', 'favorite_song': 'Hey Jude'}
    #
    #     # Post music preference
    #     response = self.client.post(reverse('MusicPreference'), data=json.dumps(music_preference_data), content_type='application/json')
    #
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)