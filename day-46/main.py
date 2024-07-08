import requests
import pprint
import time
import spotipy.oauth2
from bs4 import BeautifulSoup

link = "https://www.billboard.com/charts/hot-100/"
chosen_date = input("Enter a date in YYYY-MM-DD format: ")

response = requests.get(f"{link}/{chosen_date}")
html_of_website = response.text

soup = BeautifulSoup(html_of_website, "html.parser")
the_names = soup.find_all(name="h3", class_= "a-no-trucate")
the_singers = soup.find_all(name="span", class_= "a-no-trucate")

singers_list = []
songs_list = []
full_list = []

for names in the_names:
    songs_list.append(names.get_text().strip())

# PRACTICED
# for singer_names in the_singers:
#     singers_list.append(singer_names.get_text().strip())

# PRACTICED
# for nums in range(len(singers_list)):
#     full_list.append(f"{singers_list[nums]} - {songs_list[nums]}")

#------#_-------------_#-----------


SPOTIPY_CLIENT_ID='64ad71c57f4946bdb9ed7a65ec51a08f'
SPOTIPY_CLIENT_SECRET='81d86d5574684686ad12837cd9a1cfb8'

authentication = spotipy.oauth2.SpotifyOAuth(redirect_uri='https://dontknowbro.ge',
                                               client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               state = True,
                                               scope = "playlist-modify-private",
                                               cache_path = "token.txt",
                                               username = "31q3gouvp7mmalhbuzkaav3pigdm")

sp = spotipy.Spotify(auth_manager=authentication)
year = chosen_date.split("-")[0]

username = sp.current_user()["id"]

song_uris = []
skipped = 0
processed = 0

for name in songs_list:
    results = sp.search(q=f"track:{name} year:{year}]",type="track")
    try:
        uri = results["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        skipped += 1
    else:
        processed += 1

print(f"skipped: {skipped}, processed: {processed}")


created_playlist = sp.user_playlist_create(username, f"{chosen_date} Billboard {len(song_uris)}", public=False)

playlist_id = created_playlist["id"]

sp.user_playlist_add_tracks(username, playlist_id, song_uris, position=None)
print(f"Succesfully created playlist ({chosen_date} Billboard {len(song_uris)})")
print(f"Succesfully added {processed} songs to it!")

