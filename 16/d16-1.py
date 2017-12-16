#!/usr/bin/env python3

import sys

filename=sys.argv[1]
letter=sys.argv[2]
# av nån anledning så är det från bokstav till bokstav+1 för att få rätt längd
line=[chr(x) for x in range(ord('a'), ord(letter)+1)]

with open(filename) as f:
    input = f.readline()
    input = input.strip().split(',')
for move in input:
    if move[0]=='p':
        p1, p2 = move[1:].split('/')
        p1=line.index(p1)
        p2=line.index(p2)
        line[p1], line[p2] = line[p2], line[p1]
    elif move[0]=='s':
        offset=int(move[1:])
        line=line[-offset:]+line[:-offset];
    elif move[0]=='x':
        p1, p2 = map(int, move[1:].split('/'))
        line[p1], line[p2] = line[p2], line[p1]
print ("Answer:",''.join(line))
