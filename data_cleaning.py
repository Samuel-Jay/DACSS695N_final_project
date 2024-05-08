import os
import csv

with open('nodes.csv', newline= '\n') as f:
    reader = csv.reader(f, delimiter= ',')
    genre_artist = {}
    for row in reader:
        if row[4] == 'genre':
            continue
        else:
            for genre in row[4]:
                if genre in genre_artist.keys():
                    genre_artist[genre].append(row[1])
                elif genre not in genre_artist.keys():
                    genre_artist[genre] = [row[1]]
print(genre_artist)