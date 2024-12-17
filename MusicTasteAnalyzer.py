from collections import Counter


class MusicTasteAnalyzer:
    def __init__(self, artist_data):
        self.artist_data = artist_data

    def analyze_genres(self):
        # Flatten the genres into a single list
        all_genres = [genre for artist in self.artist_data for genre in artist['genres']]
        genre_counts = Counter(all_genres)
        return genre_counts

    def compare_with_user_taste(self, user_favorite_genres):
        genre_counts = self.analyze_genres()
        matching_genres = [genre for genre in user_favorite_genres if genre in genre_counts]
        return matching_genres
