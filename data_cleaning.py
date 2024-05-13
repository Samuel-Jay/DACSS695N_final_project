import os
import csv


edgetuples = []
with open('edges.csv', newline = '\n') as f2:
    reader2 = csv.reader(f2, delimiter = ',')
    for row in reader2:
        edgetuples.append((row[0], row[1]))
# print(len(edgetuples))

node_attrs = []
node_ids = []
with open('nodes.csv', newline = '\n') as f3:
    reader3 = csv.reader(f3, delimiter = ',')
    for row in reader3:
        node_attrs.append(row)
        node_ids.append(row[0])
# print(len(node_ids))

adjmat_buf = '"ego_spotify_id","alter_spotify_id"\n'
with open('HPedgelistprep.csv', newline = '\n') as f1:
    reader1 = csv.reader(f1, delimiter = ',')
    for row in reader1:
        for tup in edgetuples:
            if tup[0] == row[1]:
                adjmat_buf = adjmat_buf + tup[0] + ',' + tup[1] + '\n'

ff = open('HPedgelist.csv', 'w')
ff.write(adjmat_buf)
ff.close()

adjmat_buf = '"ego_spotify_id","alter_spotify_id", "alter_name", "alter_followers", "alter_genres"\n'
with open('HPedgelistprep.csv', newline = '\n') as f1:
    reader1 = csv.reader(f1, delimiter = ',')
    for row in reader1:
        for tup in edgetuples:
            if tup[0] == row[1]:
                try:
                    neighbor_index = node_ids.index(tup[1])
                except:
                    continue
                else:
                    # print('new edge')
                    adjmat_buf = adjmat_buf + tup[0] + ',' + tup[1] + ',' + str(node_attrs[neighbor_index][2]) + ',' + str(node_attrs[neighbor_index][3]) + ',"' + str(node_attrs[neighbor_index][5]) + '"\n'

fc = open('HPalter_dat.csv', 'w')
fc.write(adjmat_buf)
fc.close()
