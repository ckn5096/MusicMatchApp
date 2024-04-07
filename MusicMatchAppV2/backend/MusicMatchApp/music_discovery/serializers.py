from rest_framework import serializers
from .models import MusicPreference, Playlist, ListeningHistory


class MusicPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicPreference
        fields = ['favorite_genre', 'favorite_artist', 'favorite_song']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['name', 'tracks']


class ListeningHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeningHistory
        fields = ['user', 'tracks', 'played_at']  # Include the user, tracks, and played_at fields

