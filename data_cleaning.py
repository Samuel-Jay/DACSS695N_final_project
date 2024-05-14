import os
import csv


subgenres = []
with open('HP.csv', newline = '\n') as f:
    reader = csv.reader(f, delimiter = ',')
    for row in reader:
        genre_str = row[5][1:len(row[5]) - 1]
        curr_art_gen = genre_str.split(',')
        for cat in curr_art_gen:
            if cat not in subgenres and 'hip hop' in cat:
                subgenres.append(cat)
            else:
                continue
# print(subgenres)

genresfile = open('hiphopsubgenres.csv', 'w')
genresfile.write(str(subgenres))
genresfile.close()
