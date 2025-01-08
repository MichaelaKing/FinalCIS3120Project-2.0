import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from SpotifyDataFetcher import SpotifyDataFetcher
from MusicTasteAnalyzer import MusicTasteAnalyzer
from SpotifyDataVisualizer import SpotifyDataVisualizer 

CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'user-top-read user-read-private'


if os.path.exists(".cache"):
    os.remove(".cache")

if __name__ == "__main__":
    print("Starting Spotify authentication...")

    try:
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

        print("\nFetching top artists...")
        data_fetcher = SpotifyDataFetcher(spotify_client)
        artist_data = data_fetcher.get_top_artists(limit=10)

        if not artist_data:
            print("No artist data found.")
        else:
            print("\nTop Artists:")
            for idx, artist in enumerate(artist_data):
                print(f"{idx+1}. {artist['name']} - Genres: {', '.join(artist['genres'])}")

            # Analyze Genres
            print("\nAnalyzing genres...")
            analyzer = MusicTasteAnalyzer(artist_data)
            genre_analysis = analyzer.analyze_genres()

            print("\nGenre Analysis (Top 5):")
            for genre, count in genre_analysis.most_common(5):
                print(f"{genre}: {count} occurrences")

            
            visualizer = SpotifyDataVisualizer()
            visualizer.visualize_artist_play_counts(artist_data)
            visualizer.visualize_genre_distribution_pie(genre_analysis)

            print("\nCharts have been saved to the 'static' directory.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
