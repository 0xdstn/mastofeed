#!/usr/bin/env python3

archivedFile = open('/home/dustin/projects/mastofeed/archived.txt', 'a')

dataFile = open('/home/dustin/projects/mastofeed/data.txt', 'r+')
data = dataFile.read().splitlines()

for d in data:
    archivedFile.write(d+'\n')

dataFile.truncate(0)

archivedFile.close()
dataFile.close()
