# SpotifyDataFetcher.py - Fetches user data
class DataFetcher:
    def __init__(self, spotify_client):
        self.spotify_client = spotify_client

    def get_top_artists(self, limit=20, time_range='medium_term'):
        try:
            top_artists = self.spotify_client.current_user_top_artists(limit=limit, time_range=time_range)
            artist_data = []
            for artist in top_artists['items']:
                artist_data.append({
                    'name': artist['name'],
                    'genres': artist['genres']
                })
            return artist_data
        except Exception as e:
            print(f"Error fetching top artists: {str(e)}")
            return []

print("SpotifyDataFetcher class created successfully")

class SpotifyUserData:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        # Initialize credentials and authenticate
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope
        ))
    
    def fetch_user_top_tracks(self, limit=10):
        # Fetch user's top tracks
        results = self.sp.current_user_top_tracks(limit=limit)
        
        print("\nUser's Top Tracks:")
        tracks = []
        for idx, item in enumerate(results['items']):
            track_name = item['name']
            artist_name = item['artists'][0]['name']
            tracks.append({'Track': track_name, 'Artist': artist_name})
            print(f"{idx+1}. {track_name} - {artist_name}")
        
        return pd.DataFrame(tracks)

# User credentials and scope
CLIENT_ID = '8810837ef20d4cb7a5fdf4260e366409'
CLIENT_SECRET = '13e560bd868245e9b6dc58328837b2aa'
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'user-top-read user-read-private'

# Create an instance of the class and fetch user data
if __name__ == "__main__":
    spotify_user = SpotifyUserData(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE)
    top_tracks_df = spotify_user.fetch_user_top_tracks(limit=5)  # Fetch top 5 tracks
    
    print("\nDataFrame of Top Tracks:")
    print(top_tracks_df)


