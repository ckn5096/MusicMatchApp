from django.contrib import admin

# Register your models here.

from .models import MusicPreference , Playlist ,ListeningHistory
admin.site.register(MusicPreference)
admin.site.register(Playlist)
admin.site.register(ListeningHistory)