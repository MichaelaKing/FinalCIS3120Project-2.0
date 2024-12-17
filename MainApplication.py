import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from SpotifyDataFetcher import SpotifyDataFetcher
from MusicTasteAnalyzer import MusicTasteAnalyzer

# Spotify User Credentials and Scope
CLIENT_ID = '8810837ef20d4cb7a5fdf4260e366409'
CLIENT_SECRET = '13e560bd868245e9b6dc58328837b2aa'
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'user-top-read user-read-private'

# Clear cached token
if os.path.exists(".cache"):
    os.remove(".cache")

# Main Application
if __name__ == "__main__":
    print("Starting Spotify authentication...")

    try:
        # Authenticate with Spotify
        auth_manager = SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE,
            open_browser=False,
            cache_path=".spotify_token"
        )
        spotify_client = spotipy.Spotify(auth_manager=auth_manager)
        print("Successfully connected to Spotify!")

        # Fetch Top Artists using SpotifyDataFetcher class
        print("\nFetching top artists...")
        data_fetcher = SpotifyDataFetcher(spotify_client)
        artist_data = data_fetcher.get_top_artists(limit=10)

        if not artist_data:
            print("No artist data found.")
        else:
            # Display top artists
            print("\nTop Artists:")
            for idx, artist in enumerate(artist_data):
                print(f"{idx+1}. {artist['name']} - Genres: {', '.join(artist['genres'])}")

            # Analyze Genres using MusicTasteAnalyzer class
            print("\nAnalyzing genres...")
            analyzer = MusicTasteAnalyzer(artist_data)
            genre_analysis = analyzer.analyze_genres()

            print("\nGenre Analysis (Top 5):")
            for genre, count in genre_analysis.most_common(5):
                print(f"{genre}: {count} occurrences")

            # Compare genres with user's favorite genres
            user_favorites = ["pop", "rock", "indie"]
            matching_genres = analyzer.compare_with_user_taste(user_favorites)

            print("\nMatching Genres with User's Favorites:")
            print(matching_genres if matching_genres else "No matching genres found.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
