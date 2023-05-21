
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def scrape_playlist():
    # Set up your Spotify API credentials
    client_id = '6c685d12ac3f4e9f9de1773b0c8bbf50'
    client_secret = 'faf12cfcc5f644ba84742291044e46e8'

    # Create a Spotify client
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Extract the playlist ID from the URL
    playlist_id = '2uuGB2W5tyUxkZr2plZJPL'  # Enter the playlist ID here

    # Get the playlist tracks
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    # Create a text file to store the tracks
    file_name = 'playlist_tracks.txt'  # Choose a desired file name
    with open(file_name, 'w') as file:
        # Iterate through the tracks and extract relevant information
        for track in tracks:
            track_name = track['track']['name']
            artist_name = track['track']['artists'][0]['name']
            track_info = f"Track: {track_name} - Artist: {artist_name}\n"
            file.write(track_info)

    print(f"The tracks have been saved to {file_name}.")

    return 'The tracks have been saved.'

if __name__ == '__main__':
    app.run()

