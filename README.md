# FinalCIS3120Project-2.0
Purpose and Functionality

This project aims to provide a personalized analysis of a Spotify user's music preferences. By leveraging the Spotify API, the application retrieves the user's top artists and genres from recently, analyzes the data, and creates visualizations to represent the information effectively. Users can view:

Top Artists by Play Count (Bar Chart)

Genre Distribution (Pie Chart)

The project is designed to offer insights into a user's listening habits and genre preferences, presented in an interactive web interface. (I wanted to try and make this since spotify didnt do genres this year)

To install the program you will have to clone the url https://github.com/MichaelaKing/FinalCIS3120Project-2.0 and install certain libraries in the terminal

pip install spotipy
pip install Flask


The API credentials I used were creation of an application in Spotify Developer and using the CLIENT_ID and CLIENT_SECRET
I added http://localhost:8888/callback as a Redirect URI in the Spotify app settings.

Update Credentials in the MainApplication
Replace the following variables in the MainApplication.py file:

CLIENT_ID = '8810837ef20d4cb7a5fdf4260e366409'
CLIENT_SECRET = '13e560bd868245e9b6dc58328837b2aa'
REDIRECT_URI = 'http://localhost:8888/callback'

1. Create a static directory to make sure the charts are sent there
2. Run the main application first to Authentic. This will open a new browser. You will need to copy the link in the browser and paste it to the terminal. 
3. You will get your top artists genre results in the terminal and your static folder should be populated with you charts. 
4. Run the Testeer file to open the web browser with all of your info
