import pandas as pd

class GetPopularGenres:
  
    
      def get_global_popular_genres_from_csv(file_path):
        file_path = '/workspaces/FinalCIS3120Project-2.0/data_by_genres.csv'
        popular_genres = {}

        try:
            
            genre_data = pd.read_csv(file_path)

            if 'genres' in genre_data.columns and 'popularity' in genre_data.columns:
                genre_grouped = genre_data.groupby('genres')['popularity'].sum()
                popular_genres = genre_grouped.to_dict()
            else:
                print("Error: Required columns 'genres' and 'popularity' not found in CSV.")

        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"Error reading CSV file: {str(e)}")

        return popular_genres
