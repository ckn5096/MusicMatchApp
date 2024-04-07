from django.test import TestCase
from ..models import MusicPreference, Playlist



from django.contrib.auth.models import User

class MusicPreferenceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_music_preference_creation(self):
        music_preference = MusicPreference.objects.create(
            user=self.user,
            favorite_genre='Rock',
            favorite_artist='The Beatles',
            favorite_song='Hey Jude'
        )
        self.assertEqual(music_preference.__str__(), f"Music Preference for {self.user.username}")

class PlaylistModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_playlist_creation(self):
        playlist = Playlist.objects.create(
            user=self.user,
            name='Test Playlist',
            tracks=['Track 1', 'Track 2']
        )
        self.assertEqual(playlist.__str__(), f"Playlist 'Test Playlist' for {self.user.username}")
