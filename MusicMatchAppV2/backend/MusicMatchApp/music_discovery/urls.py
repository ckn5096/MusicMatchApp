from django.urls import path
<<<<<<< HEAD
from .views import MusicPreferenceView, GeneratePlaylistView, UserPlaylistsView
=======
from .views import MusicPreferenceView, GeneratePlaylistView, UserPlaylistsView , SpotifyLoginView , SpotifyCallbackView, ListeningHistoryView
>>>>>>> origin/master

urlpatterns = [
   # path('register/', RegistrationView.as_view(), name='registration'),
    #path('login/', LoginView.as_view(), name='login'),
    #path('home/', HomeView.as_view(), name='home'),

    path('MusicPreference/', MusicPreferenceView.as_view(), name='MusicPreference'),
    path('generate_playlist/', GeneratePlaylistView.as_view(), name='GeneratePlaylist'),
    path('UserPlaylist/', UserPlaylistsView.as_view(), name='UserPlaylist'),
<<<<<<< HEAD
=======
    path('api/Spotify/login', SpotifyLoginView.as_view(), name='SpotifyLogin'),
    path('spotify-callback/', SpotifyCallbackView.as_view(), name='spotify_callback'),
    path('api/ListeningHistory/', ListeningHistoryView.as_view(), name='ListeningHistory'),
>>>>>>> origin/master
]

