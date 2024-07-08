import spotipy
import spotipy.oauth2


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

for
results = sp.search(q=f"track:Rockstar year:2020",type="track")
uri = results["tracks"]["items"][0]["uri"]
print(uri)



