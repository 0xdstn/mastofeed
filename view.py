#!/usr/bin/env python3

import html
import re 

dataFile = open('/home/dustin/projects/mastofeed/data.txt', 'r')
data = sorted(dataFile.read().splitlines())

TAG_RE = re.compile(r'<[^>]+>')

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
BOLD  = "\033[;1m"
GREY  = "\033[1;30;40m"
RESET = "\033[0;0m"

def render(text):
    text = d[2].replace('</p>','\n').replace('<p>','')
    text = text.strip('\n')
    text = html.unescape(text)
    text = TAG_RE.sub('', text)
    print(text)

def printLine():
    print(BOLD + '--------------------------------------------------------' + RESET)

def color(color,text):
    print(color+text+RESET)

for line in data:
    d = line.split('|')
    name = d[1].split('/@')[1].split('/')[0]
    inst = d[1].split('//')[1].split('/')[0]
    print('')
    print('')
    printLine()
    color(GREY,d[0])
    print(CYAN + name + RESET + '@' + BLUE + inst + RESET)
    color(GREY,d[1])
    printLine()
    render(d[2])
    if len(d) > 3:
        print('')
        color(BOLD,'MEDIA')
        media = d[3].split('*')
        for m in media:
            color(GREY,m)
    printLine()

dataFile.close()

