from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MusicPreference, Playlist
from .serializers import MusicPreferenceSerializer, PlaylistSerializer, ListeningHistorySerializer
from rest_framework.permissions import BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
import requests
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
<<<<<<< HEAD

import spotipy
=======
from datetime import datetime, timedelta

import spotipy
from spotipy import Spotify
>>>>>>> origin/master
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials


class IsTokenAuthenticated(BasePermission):
    """
    Custom permission to authenticate users using token from local storage.
    """

    def has_permission(self, request, view):
        token_key = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
        try:
            token = Token.objects.get(key=token_key)
            request.user = token.user
            return True
        except Token.DoesNotExist:
            raise AuthenticationFailed('Token is invalid or expired')


class MusicPreferenceView(APIView):
    permission_classes = [IsTokenAuthenticated]
    authentication_classes = [TokenAuthentication]

    # def get(self, request):
    #     try:
    #         # Get the music preference for the authenticated user
    #         music_preference = MusicPreference.objects.get(user=request.user)
    #         serializer = MusicPreferenceSerializer(music_preference)
    #         return Response(serializer.data)
    #     except MusicPreference.DoesNotExist:
    #         return Response({'message': 'No music preference set for this user'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        try:
            # Attempt to retrieve the music preference for the authenticated user
            music_preference = MusicPreference.objects.get(user=request.user)
            serializer = MusicPreferenceSerializer(music_preference)
            return Response(serializer.data)
        except MusicPreference.DoesNotExist:
            # If the preference does not exist, return a default null value
            return Response({'message': 'No music preference set for this user', 'music_preference': None},
                            status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MusicPreferenceSerializer(data=request.data)
        if serializer.is_valid():
            # Associate the music preference with the authenticated user
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        music_preference = MusicPreference.objects.get(user=request.user)
        serializer = MusicPreferenceSerializer(music_preference, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        music_preference = MusicPreference.objects.get(user=request.user)
        music_preference.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class GeneratePlaylistView(APIView):
    permission_classes = [IsTokenAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        preferences = request.data

        # Get the user associated with the token
        token_key = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
        try:
            token = Token.objects.get(key=token_key)
            user = token.user
        except Token.DoesNotExist:
            raise AuthenticationFailed('Token is invalid or expired')

        # Initialize Spotipy client with Spotify Developer API credentials
        sp = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id='71b57beac4374097b7fa168d2f2403bd',
                                                                client_secret='917821889f14406db3ecc8427ab7ac67'))

        # Get Spotify ID for the favorite artist
        artist_name = preferences.get('favorite_artist', '')
        if artist_name:
            # Search for the artist
            results = sp.search(q=artist_name, type='artist')
            artists = results['artists']['items']
            if artists:
                # Get the Spotify ID of the first artist in the search results
                favorite_artist_id = artists[0]['id']
            else:
                # Handle case where no artist is found
                return Response({'error': 'Favorite artist not found'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Handle case where favorite_artist is missing
            return Response({'error': 'Favorite artist is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Use user's preferences to generate recommended tracks
        recommended_tracks = sp.recommendations(seed_artists=[favorite_artist_id], limit=10)

        # # Extract relevant information from recommended tracks
        # recommended_songs = [{
        #     'name': track['name'],
        #     'artist': ', '.join([artist['name'] for artist in track['artists']]),
        #     'album': track['album']['name'],
        #     'uri': track['uri']
        # } for track in recommended_tracks['tracks']]

        # Extract relevant information from recommended tracks, including song art URLs
        recommended_songs = []
        for track in recommended_tracks['tracks']:
            # Extract song art URLs
            album_art_urls = [image['url'] for image in track['album']['images']]
            # Extract track ID from the URI
            track_id = track['uri'].split(':')[-1]
            # Construct Spotify track URL
            spotify_track_url = f"https://open.spotify.com/track/{track_id}"
            # Append track data with song art URLs
            recommended_songs.append({
                'name': track['name'],
                'artist': ', '.join([artist['name'] for artist in track['artists']]),
                'album': track['album']['name'],
                'uri': track['uri'],
                'album_art_urls': album_art_urls,  # Include song art URLs in the data
                'track_id': track_id,  # Include track ID in the data
                'spotify_track_url': spotify_track_url  # Include Spotify track URL in the data

            })

        # Save the generated playlist to the database with the user
        playlist_data = {
            'name': 'Generated Playlist',  # You can customize the name as needed
            'tracks': recommended_songs
        }
        playlist_serializer = PlaylistSerializer(data=playlist_data)
        if playlist_serializer.is_valid():
            playlist_serializer.save(user=user)
            return Response(playlist_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(playlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserPlaylistsView(APIView):
    permission_classes = [IsTokenAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user  # Assuming you're using Django's built-in authentication
        playlists = Playlist.objects.filter(user=user)
        # Serialize playlists data and return it in the response
        playlists_data = []  # Assuming you have a serializer to serialize playlist data
        for playlist in playlists:
            playlist_data = {
                'name': playlist.name,
                'tracks': playlist.tracks,
                # 'song_art_urls': playlist.song_art_url,  # Include song art URLs in response
                # Add other fields as needed
            }
            playlists_data.append(playlist_data)
        return Response(playlists_data, status=status.HTTP_200_OK)



    def delete(self, request):
        playlist_user = Playlist.objects.get(user=request.user)
        playlist_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

<<<<<<< HEAD
=======


# class ListeningHistoryView(APIView):
#     permission_classes = [IsTokenAuthenticated]
#     authentication_classes = [TokenAuthentication]
#
#     def get(self, request):
#         # Get user object
#         user = request.user
#
#         # Get access token from user's session
#         # access_token = request.session.get('spotify_access_token')
#         access_token = 'BQDeAH36KeqSXw_rXeCJO9fijnlVgNarJizwrLRfpZuu27uN32LMA59SoshfdS7iOkwxyiA4Welr7jqXnPS0MFsfpFSPvlh59TIMkAMIJ_f8fIBrHu3dWwPNnLZq4zNrLlVLbI9_5cHbtRhkq7vZYd6qWuy0e20-nVWWM09R4KcmDQnSOu0pDhP68eTO5HzqDK0WhNLEzQZyW_RFzmksdVPx'
#
#         if access_token:
#             # Initialize Spotify client with the access token
#             sp = Spotify(auth=access_token)
#
#             # Fetch the user's listening history
#             listening_history = sp.current_user_recently_played(limit=15)
#
#             # Extract relevant information from listening history
#             tracks_data = []
#             for item in listening_history['items']:
#                 track_data = {
#                     'track_name': item['track']['name'],
#                     'artist_name': ', '.join([artist['name'] for artist in item['track']['artists']]),
#                     'album_name': item['track']['album']['name'],
#                     'uri': item['track']['uri'],
#                     'played_at': item['played_at']
#                 }
#                 tracks_data.append(track_data)
#
#                 # Create instances of ListeningHistorySerializer with provided data
#             listening_history_data = {
#                     'user': request.user.id,  # Assuming user is authenticated and user id is accessible
#                     'tracks': tracks_data
#                 }
#
#             listening_history_serializer = ListeningHistorySerializer(data=listening_history_data)
#             if listening_history_serializer.is_valid():
#                 listening_history_serializer.save()
#                 return Response(listening_history_serializer.data, status=status.HTTP_200_OK)
#             else:
#                 return Response(listening_history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


>>>>>>> origin/master
class ListeningHistoryView(APIView):
    permission_classes = [IsTokenAuthenticated]
    authentication_classes = [TokenAuthentication]

<<<<<<< HEAD
    def get(self, request):
        # Get user's Spotify listening history
        sp = spotipy.Spotify(auth=request.user.spotify_access_token)  # Assuming you have stored Spotify access token for the user
        listening_history = sp.current_user_recently_played(limit=10)  # Fetch the last 10 tracks from the user's listening history

        # Extract relevant information from listening history
        tracks_data = []
        for item in listening_history['items']:
            track_data = {
                'track_name': item['track']['name'],
                'artist_name': ', '.join([artist['name'] for artist in item['track']['artists']]),
                'album_name': item['track']['album']['name'],
                'uri': item['track']['uri'],
                'played_at': item['played_at']
            }
            tracks_data.append(track_data)

        # Save the listening history to the database
        listening_history_serializer = ListeningHistorySerializer(data=tracks_data, many=True)
        if listening_history_serializer.is_valid():
            listening_history_serializer.save(user=request.user)
            return Response(listening_history_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(listening_history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpotifyLoginView(APIView):
=======
    def get_access_token(self, request):
        # Check if access token is present and not expired
        access_token = request.query_params.get('access_token')
        token_expiry = request.query_params.get('token_expiry')

        if access_token and token_expiry:
            expiry_time = datetime.fromisoformat(token_expiry)
            if expiry_time > datetime.now() + timedelta(minutes=5):  # Refresh token 5 minutes before expiry
                return access_token

        # If access token is expired or not present, return None
        return None

    def get(self, request):
        # Get user object
        user = request.user

        # Get access token from local storage or query parameters
        access_token = self.get_access_token(request)

        print('Access token:', access_token)

        if access_token:
            # Initialize Spotify client with the access token
            sp = Spotify(auth=access_token)

            # Fetch the user's listening history
            listening_history = sp.current_user_recently_played(limit=15)

            # Extract relevant information from listening history
            tracks_data = []
            for item in listening_history['items']:
                track_data = {
                    'track_name': item['track']['name'],
                    'artist_name': ', '.join([artist['name'] for artist in item['track']['artists']]),
                    'album_name': item['track']['album']['name'],
                    'uri': item['track']['uri'],
                    'played_at': item['played_at']
                }
                tracks_data.append(track_data)

                # Create instances of ListeningHistorySerializer with provided data
            listening_history_data = {
                    'user': request.user.id,  # Assuming user is authenticated and user id is accessible
                    'tracks': tracks_data
                }

            # Return the data to the frontend along with the access token and its expiry
            response_data = {
                'access_token': access_token,
                'token_expiry': (datetime.now() + timedelta(days=1)).isoformat(),  # Example expiry time (1 day)
                'tracks': tracks_data
            }

            listening_history_serializer = ListeningHistorySerializer(data=listening_history_data)

        if listening_history_serializer.is_valid():
            listening_history_serializer.save()
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # If access token is not valid, return an error response
            return Response({'error': 'Invalid access token'}, status=status.HTTP_401_UNAUTHORIZED)


class SpotifyLoginView(APIView):
    authentication_classes = []

>>>>>>> origin/master
    def get(self, request):
        # Define Spotify OAuth parameters
        client_id = settings.SPOTIFY_CLIENT_ID
        redirect_uri = request.build_absolute_uri(reverse('spotify_callback'))
<<<<<<< HEAD
        scope = 'user-read-private user-read-email'  # Specify required scopes
=======
        scope = 'user-read-private user-read-email user-read-recently-played'  # Include the user-read-recently-played scope
>>>>>>> origin/master

        # Construct Spotify authorization URL
        auth_url = f'https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}'

        # Redirect user to Spotify authorization page
<<<<<<< HEAD
        return redirect(auth_url)

class SpotifyCallbackView(APIView):
=======
        return Response({'auth_url': auth_url})
        # return redirect(auth_url)

# class SpotifyCallbackView(APIView):
#
#     def get(self, request):
#         # Get authorization code from callback URL
#         code = request.GET.get('code')
#
#         # Exchange authorization code for access token
#         access_token_url = 'https://accounts.spotify.com/api/token'
#         client_id = settings.SPOTIFY_CLIENT_ID
#         client_secret = settings.SPOTIFY_CLIENT_SECRET
#         redirect_uri = request.build_absolute_uri(reverse('spotify_callback'))
#
#         data = {
#             'grant_type': 'authorization_code',
#             'code': code,
#             'redirect_uri': redirect_uri,
#             'client_id': client_id,
#             'client_secret': client_secret,
#         }
#
#         response = requests.post(access_token_url, data=data)
#         token_data = response.json()
#
#         # Store access token in session or database
#         access_token = token_data['access_token']
#         request.session['spotify_access_token'] = access_token
#
#         print("code: " , code)
#         print("Access Token : " , access_token)
#
#         # Redirect user to a success page or dashboard
#         return redirect('http://localhost:3000/home/')


class SpotifyCallbackView(APIView):

>>>>>>> origin/master
    def get(self, request):
        # Get authorization code from callback URL
        code = request.GET.get('code')

        # Exchange authorization code for access token
        access_token_url = 'https://accounts.spotify.com/api/token'
        client_id = settings.SPOTIFY_CLIENT_ID
        client_secret = settings.SPOTIFY_CLIENT_SECRET
        redirect_uri = request.build_absolute_uri(reverse('spotify_callback'))

        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri,
            'client_id': client_id,
            'client_secret': client_secret,
        }

        response = requests.post(access_token_url, data=data)
        token_data = response.json()

<<<<<<< HEAD
        # Store access token in session or database
        access_token = token_data['access_token']
        request.session['spotify_access_token'] = access_token

        # Redirect user to a success page or dashboard
        return redirect('dashboard')
=======
        # Store access token in local storage and include it in the redirection URL
        access_token = token_data['access_token']
        token_expiry = (datetime.now() + timedelta(hours=1)).isoformat()  # Example expiry time (1 day)
        # redirect_url = f'http://localhost:3000/home/?access_token={access_token}&token_expiry={token_expiry}'
        redirect_url = f'http://localhost:3000/ListeningHistory/?access_token={access_token}&token_expiry={token_expiry}'

        return redirect(redirect_url)
>>>>>>> origin/master
