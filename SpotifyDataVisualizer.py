import matplotlib.pyplot as plt

class SpotifyDataVisualizer:
    @staticmethod
    def visualize_artist_play_counts(artist_data, save_path="static/artist_play_counts.png"):
        if not artist_data:
            print("No artist data available to visualize.")
            return

        artist_names = [artist['name'] for artist in artist_data]
        play_counts = [artist.get('play_count', 0) for artist in artist_data]

        plt.figure(figsize=(12, 6))
        plt.bar(artist_names, play_counts, color='coral')
        plt.xticks(rotation=45, ha='right')
        plt.title("Top Artists by Play Count")
        plt.xlabel("Artists")
        plt.ylabel("Play Count")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

    @staticmethod
    def visualize_genre_distribution_pie(genre_data, save_path="static/genre_distribution_pie.png"):
        if not genre_data:
            print("No genre data available to visualize.")
            return

        genres = list(genre_data.keys())
        counts = list(genre_data.values())

        plt.figure(figsize=(8, 8))
        plt.pie(counts, labels=genres, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
        plt.title("Genre Distribution")
        plt.savefig(save_path)
        plt.close()
