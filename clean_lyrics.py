import re


def clean_lyrics(original_lyrics):
    original_lyrics = original_lyrics.lower()

    original_lyrics = re.sub("[\(\[].*?[\)\]]", "", original_lyrics)

    lyrics = ""

    for char in original_lyrics:
        if char == "\n" or ord(char) in range(97, 123) or ord(char) == 32:
            lyrics += char

    lyrics = lyrics.split("\n")

    for i, line in enumerate(lyrics):
        lyrics[i] = lyrics[i].split()

    for line in lyrics:
        if not line:
            lyrics.remove(line)

    cleaned_lyrics = ""

    for line in lyrics:
        for i, word in enumerate(line):
            cleaned_lyrics += word
            if i + 1 != len(line):
                cleaned_lyrics += " "
        cleaned_lyrics += "\n"

    return cleaned_lyrics
