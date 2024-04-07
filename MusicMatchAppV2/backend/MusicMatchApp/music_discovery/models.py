from django.db import models
<<<<<<< HEAD
# from ..MusicMatchApp import settings
=======
#from ..MusicMatchApp import settings
>>>>>>> origin/master


from django.conf import settings

<<<<<<< HEAD

# Create your models here.

class MusicPreference(models.Model):
    objects = None
=======
# Create your models here.

class MusicPreference(models.Model):
>>>>>>> origin/master
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favorite_genre = models.CharField(max_length=100)
    favorite_artist = models.CharField(max_length=100)
    favorite_song = models.CharField(max_length=100)

    def __str__(self):
        return f"Music Preference for {self.user.username}"


<<<<<<< HEAD
=======

>>>>>>> origin/master
class Playlist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tracks = models.JSONField()  # Store track data as JSON

<<<<<<< HEAD
=======

>>>>>>> origin/master
    def __str__(self):
        return f"Playlist '{self.name}' for {self.user.username}"


# class ListeningHistory(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     track_name = models.CharField(max_length=255)
#     artist_name = models.CharField(max_length=255)
#     album_name = models.CharField(max_length=255)
#     uri = models.CharField(max_length=255)
#     played_at = models.DateTimeField()
#
#     def __str__(self):
#         return f"{self.track_name} - {self.artist_name} ({self.played_at})"

class ListeningHistory(models.Model):
<<<<<<< HEAD
    objects = None
=======
>>>>>>> origin/master
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tracks = models.JSONField()  # Store listening history as JSON
    played_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the track was played

    def __str__(self):
<<<<<<< HEAD
        return f"Listening History for {self.user.username} ({self.played_at})"
=======
        return f"Listening History for {self.user.username} ({self.played_at})" 

>>>>>>> origin/master
