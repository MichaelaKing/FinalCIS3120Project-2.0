import matplotlib.pyplot as plt

class GenrePopularityVisualizer:
    
    def plot_genre_comparison(genre_comparison):
    
        genres = list(genre_comparison.keys())
        user_counts = [stats['user_count'] for stats in genre_comparison.values()]
        global_counts = [stats['global_count'] for stats in genre_comparison.values()]

        total_user = sum(user_counts)
        total_global = sum(global_counts)

        if total_user == 0 or total_global == 0:
            print("No data available for visualization.")
            return

        user_percentages = [count / total_user * 100 for count in user_counts]
        global_percentages = [count / total_global * 100 for count in global_counts]

        fig, axs = plt.subplots(1, 2, figsize=(14, 7))

        axs[0].pie(user_percentages, labels=genres, autopct='%1.1f%%', startangle=140)
        axs[0].set_title("User's Genre Preferences")

        axs[1].pie(global_percentages, labels=genres, autopct='%1.1f%%', startangle=140)
        axs[1].set_title("Global Genre Popularity")

        plt.tight_layout()
        plt.show()
