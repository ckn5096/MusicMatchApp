# backend/MusicMatchApp/music_discovery/recommendation_engine.py
from django.contrib.auth.models import User
from django.db.models import Count
from MusicMatchAppV2.backend.MusicMatchApp.music_discovery.models import MusicPreference, ListeningHistory
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def user_profiling(user_id):
    try:
        user = User.objects.get(pk=user_id)

        # Collect user preferences
        music_preference = MusicPreference.objects.get(user=user)

        # Update user interactions (listening history)
        listening_history = ListeningHistory.objects.filter(user=user)

        # Example: Calculate the most listened-to genre
        most_listened_genre = listening_history.values('tracks__genre').annotate(count=Count('id')).order_by(
            '-count').first()

        # You can add more logic here to update other preferences and interactions

        return {
            'music_preference': music_preference,
            'listening_history': listening_history,
            'most_listened_genre': most_listened_genre,
            # Add more user profile data as needed
        }
    except User.DoesNotExist:
        return None


class MusicRecommendation:
    def __init__(self, music_data, user_preferences=None):
        self.music_data = music_data
        self.user_preferences = user_preferences if user_preferences else {}
        self.tfidf_matrix = None
        self.similarity_matrix = None
        self.track_indices = pd.Series(music_data.index, index=music_data['Track Name']).drop_duplicates()

    def preprocess_data(self):
        # Concatenate relevant features for TF-IDF vectorization
        self.music_data['Features'] = self.music_data['Genre'] + ' ' + self.music_data['Artist']

        # Initialize TF-IDF Vectorizer
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')

        # Fit and transform the data
        self.tfidf_matrix = tfidf_vectorizer.fit_transform(self.music_data['Features'])

        # Compute the cosine similarity matrix
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def recommend_music(self, track_name, num_recommendations=5):
        # Get the index of the track
        track_index = self.track_indices[track_name]

        # Get the pairwise similarity scores of all tracks with that track
        similarity_scores = list(enumerate(self.similarity_matrix[track_index]))

        # Sort the tracks based on similarity scores
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

        # Get the top n most similar tracks
        similar_tracks_indices = [i[0] for i in similarity_scores[1:num_recommendations + 1]]

        # Return the names of the most similar tracks
        return self.music_data['Track Name'].iloc[similar_tracks_indices]


class RecommendationSystem:
    def __init__(self):
        pass

    def generate_recommendations(self, user):
        # Retrieve the user's listening history
        listening_history = ListeningHistory.objects.filter(user=user)

        # Retrieve the user's music preferences
        music_preference = MusicPreference.objects.get(user=user)

        # Convert the listening history queryset to a pandas DataFrame
        history_data = pd.DataFrame(list(listening_history.values('tracks__name', 'tracks__genre', 'tracks__artist')))

        # Initialize MusicRecommendation object
        music_recommendation = MusicRecommendation(history_data)

        # Preprocess the data
        music_recommendation.preprocess_data()

        # Generate music recommendations
        recommendations = music_recommendation.recommend_music(history_data['tracks__name'].iloc[0])

        return recommendations
