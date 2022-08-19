import random

# First use lyric_grabber.py to get lyrics to be used

file_name = ".txt" # Fill in name of file with lyrics
length = 100

full = {}


class Node:
    def __init__(self, nodes):
        self.neighbours = {}
        self.nodes = nodes
        self.total = 0

    def add_word(self, word):
        self.total += 1
        if word in self.neighbours:
            self.neighbours[word][1] += 1
        elif word in self.nodes:
            self.neighbours[word] = [self.nodes[word], 1]
        else:
            self.nodes[word] = Node(self.nodes)
            self.neighbours[word] = [self.nodes[word], 1]

    def get_next_word(self):
        choice = random.randint(1, self.total)
        for current_word in self.neighbours:
            if choice <= self.neighbours[current_word][1]:
                return current_word
            else:
                choice -= self.neighbours[current_word][1]


storage = open(file_name)
lyrics = storage.read().split("\n")
storage.close()

clean_lyrics = []

for line in lyrics:
    for word in line.split():
        clean_lyrics.append(word)
    clean_lyrics.append("\n")

full[clean_lyrics[0]] = Node(full)

for i, word in enumerate(clean_lyrics):
    if i < len(clean_lyrics) - 1:
        full[word].add_word(clean_lyrics[i + 1])
    else:
        full[word].add_word("\n")

next_word = random.choice(clean_lyrics)
sentence = ""

for i in range(length):
    sentence += " " + next_word
    next_word = full[next_word].get_next_word()

print(sentence)
