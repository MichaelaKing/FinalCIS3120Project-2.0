import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, render_template_string, url_for
import webbrowser
import threading
from SpotifyDataFetcher import SpotifyDataFetcher
from MusicTasteAnalyzer import MusicTasteAnalyzer
from SpotifyDataVisualizer import SpotifyDataVisualizer

CLIENT_ID = '8810837ef20d4cb7a5fdf4260e366409'
CLIENT_SECRET = '13e560bd868245e9b6dc58328837b2aa'
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'user-top-read user-read-private'

if os.path.exists(".cache"):
    os.remove(".cache")

app = Flask(__name__)

@app.route("/")
def display_spotify_data():
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

        data_fetcher = SpotifyDataFetcher(spotify_client)
        artist_data = data_fetcher.get_top_artists(limit=10)

        analyzer = MusicTasteAnalyzer(artist_data)
        genre_analysis = analyzer.analyze_genres()

        visualizer = SpotifyDataVisualizer()
        visualizer.visualize_genre_distribution_pie(genre_analysis, save_path="static/genre_distribution_pie.png")
        visualizer.visualize_artist_play_counts(artist_data, save_path="static/artist_play_counts.png")

        html_template = """
        <html>
            <head>
                <title>Spotify Top Artists</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        max-width: 800px;
                        margin: 40px auto;
                        padding: 20px;
                        line-height: 1.6;
                        background-color: black;
                        color: white;
                    }

                    .title {
                        text-align: center;
                        font-size: 36px;
                        font-weight: bold;
                        margin-bottom: 30px;
                        text-transform: uppercase;
                        letter-spacing: 2px;
                        border-bottom: 2px solid white;
                        padding-bottom: 20px;
                    }

                    h2 {
                        font-size: 24px;
                        margin-top: 40px;
                        margin-bottom: 20px;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                    }

                    ul {
                        list-style-type: none;
                        padding: 0;
                    }

                    li {
                        margin-bottom: 10px;
                        font-size: 18px;
                    }

                    .charts {
                        text-align: center;
                        margin-top: 20px;
                    }

                    .error {
                        color: red;
                        font-weight: bold;
                        text-align: center;
                        margin-top: 20px;
                    }
                </style>
            </head>
            <body>
                <img src="{{ url_for('static', filename='Full_Logo_Green_RGB.svg') }}" alt="Spotify Logo" style="display: block; margin: 0 auto; width: 200px;">
                <h1 class="title">Spotify Top Artists</h1>

                {% if artist_data %}
                    <h2>Top Artists</h2>
                    <ul>
                        {% for artist in artist_data %}
                            <li>{{ loop.index }}. {{ artist['name'] }} - Genres: {{ ", ".join(artist['genres']) }}</li>
                        {% endfor %}
                    </ul>

                    <h2>Genre Analysis</h2>
                    <div class="charts">
                        <img src="{{ url_for('static', filename='genre_distribution_pie.png') }}" alt="Genre Distribution" style="width: 100%; max-width: 500px; margin-bottom: 20px;">
                        <img src="{{ url_for('static', filename='artist_play_counts.png') }}" alt="Artist Play Counts" style="width: 100%; max-width: 500px;">
                    </div>
                {% else %}
                    <p class="error">No artist data found. Try listening to some music on Spotify!</p>
                {% endif %}
            </body>
        </html>
        """

        return render_template_string(html_template, artist_data=artist_data, genre_analysis=genre_analysis)

    except Exception as e:
        return f"<h1>Error</h1><p>{str(e)}</p>"

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=False)
