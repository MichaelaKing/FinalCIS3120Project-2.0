import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, render_template_string
import webbrowser
import threading
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

# Flask App Setup
app = Flask(__name__)

@app.route("/")
def display_spotify_data():
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

        # Fetch Top Artists
        data_fetcher = SpotifyDataFetcher(spotify_client)
        artist_data = data_fetcher.get_top_artists(limit=10)

        # Analyze Genres
        analyzer = MusicTasteAnalyzer(artist_data)
        genre_analysis = analyzer.analyze_genres()

        # HTML Template for Display
        html_template = """
        <html>
        <head><title>Spotify Top Artists</title></head>
        <body>
            <h1>Spotify Top Artists</h1>
            {% if artist_data %}
                <h2>Top Artists</h2>
                <ul>
                {% for artist in artist_data %}
                    <li>{{ loop.index }}. {{ artist['name'] }} - Genres: {{ ", ".join(artist['genres']) }}</li>
                {% endfor %}
                </ul>
                <h2>Genre Analysis</h2>
                <ul>
                {% for genre, count in genre_analysis.items() %}
                    <li>{{ genre }}: {{ count }} occurrences</li>
                {% endfor %}
                </ul>
            {% else %}
                <p>No artist data found. Try listening to some music on Spotify!</p>
            {% endif %}
        </body>
        </html>
        """

        # Render the HTML Template
        return render_template_string(html_template, artist_data=artist_data, genre_analysis=genre_analysis)

    except Exception as e:
        return f"<h1>Error</h1><p>{str(e)}</p>"

def open_browser():
    """
    Automatically opens the browser to the Flask app after Spotify OAuth.
    """
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    # Open browser in a separate thread
    threading.Timer(1, open_browser).start()

    # Start the Flask server
    app.run(debug=False)
