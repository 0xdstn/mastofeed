#!/usr/bin/env python3

import requests
import xmltodict
import datetime

followingFile = open('following.txt', 'r') #opens the file in read mode
following = followingFile.read().splitlines() #puts the file into an array
followingFile.close()

archivedFile = open('archived.txt', 'r')
archived = archivedFile.read()
archivedFile.close()

dataFile = open('data.txt', 'r+')
data = dataFile.read()

for user in following:
    inf = user.split('@')
    url = 'https://' + inf[1] + '/users/' + inf[0] + '.rss'
    resp = requests.get(url)
    xml = xmltodict.parse(resp.content)
    channel = xml['rss']['channel']
    for x in channel:
        if x == 'item':
            for y in channel[x]:
                if y['link'] not in data and y['link'] not in archived: 
                    d = datetime.datetime.strptime(y['pubDate'], '%a, %d %b %Y %H:%M:%S %z')
                    newDate = d.strftime('%Y-%m-%d %H:%M:%S')
                    line = newDate + '|' + y['link'] + '|' + y['description']
                    if 'enclosure' in y.keys():
                        line += '|'
                        if isinstance(y['enclosure'],list):
                            for z in y['enclosure']:
                                line += z['@url']
                                line += '*'
                        else:
                            line += y['enclosure']['@url']

                        line = line.strip('*')
                    dataFile.write(line + '\n')
dataFile.close()
