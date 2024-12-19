import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyDataFetcher:
    def __init__(self, spotify_client):
        self.spotify_client = spotify_client

    def get_top_artists(self, limit=20, time_range='medium_term'):
        try:
            top_artists = self.spotify_client.current_user_top_artists(limit=limit, time_range=time_range)
            artist_data = []
            for artist in top_artists['items']:
                artist_data.append({
                    'name': artist['name'],
                    'genres': artist['genres'],
                    'play_count': artist.get('popularity', 0) 
                })
            return artist_data
        except Exception as e:
            print(f"Error fetching top artists: {str(e)}")
            return []
