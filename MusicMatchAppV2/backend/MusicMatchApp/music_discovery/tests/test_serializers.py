from django.test import TestCase
from ..serializers import MusicPreferenceSerializer, PlaylistSerializer
from ..models import MusicPreference, Playlist
from django.contrib.auth.models import User

class MusicPreferenceSerializerTest(TestCase):
    def test_valid_music_preference_serializer(self):
        user = User.objects.create_user(username='testuser', password='12345')
        music_preference_data = {'user': user.id, 'favorite_genre': 'Rock', 'favorite_artist': 'The Beatles', 'favorite_song': 'Hey Jude'}
        serializer = MusicPreferenceSerializer(data=music_preference_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_music_preference_serializer(self):
        music_preference_data = {'favorite_genre': 'Rock', 'favorite_artist': 'The Beatles'}  # Missing 'favorite_song'
        serializer = MusicPreferenceSerializer(data=music_preference_data)
        self.assertFalse(serializer.is_valid())

class PlaylistSerializerTest(TestCase):
    def test_valid_playlist_serializer(self):
        user = User.objects.create_user(username='testuser', password='12345')
        playlist_data = {'user': user.id, 'name': 'Test Playlist', 'tracks': ['Track 1', 'Track 2']}
        serializer = PlaylistSerializer(data=playlist_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_playlist_serializer(self):
        playlist_data = {'name': 'Test Playlist'}  # Missing 'tracks'
        serializer = PlaylistSerializer(data=playlist_data)
        self.assertFalse(serializer.is_valid())
