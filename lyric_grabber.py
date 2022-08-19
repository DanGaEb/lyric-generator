import clean_lyrics
import get_lyrics
import sys

# Set to True and add link to artist on azlyrics.com if you want all their songs
all_of_artist = True
artist_url = ""

# Set above to False and add links to songs on AZLyrics
playlist = """song1 url
song2 url
etc.""".split("\n")

# Choose file to store lyrics in (e.g. artist.txt)
file_name = ".txt"

if all_of_artist:
    playlist = get_lyrics.get_songs(artist_url)
    if len(playlist) == 0:
        print("Potentially blocked by AZLyrics, please try another artist or try again later")
        sys.exit()

storage = open(file_name, "w")

for song in playlist:
    try:
        lyrics = get_lyrics.get_lyrics(song)
    except IndexError:
        print("Blocked by AZLyrics, proceeding with lyrics download so far")
        storage.close()
        sys.exit()

    storage.write(clean_lyrics.clean_lyrics(lyrics))

storage.close()
