import requests
import time
from bs4 import BeautifulSoup


def get_songs(url):
    data = requests.get(url)

    html = BeautifulSoup(data.text, "html.parser")
    songs = html.select(".listalbum-item")

    song_urls = []

    for song in songs:
        song_urls.append("https://azlyrics.com" + song.select("a")[0]["href"])

    return song_urls


def get_lyrics(url):
    time.sleep(1) # Helps prevent being blocked by AZLyrics

    data = requests.get(url)

    html = BeautifulSoup(data.text, "html.parser")

    lyrics = html.select(".text-center")

    temp_lyrics = lyrics[3].text.split("\n")

    lyrics = []

    for line in temp_lyrics:
        if line != "":
            lyrics.append(line)

    return "\n".join(lyrics[4:lyrics.index(" Submit Corrections")])
