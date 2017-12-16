#!/usr/bin/env python3

import sys

filename=sys.argv[1]
letter=sys.argv[2]
# av nån anledning så är det från bokstav till bokstav+1 för att få rätt längd
line=[chr(x) for x in range(ord('a'), ord(letter)+1)]
seen = set()

def dance(input):
    global line
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

with open(filename) as f:
    input = f.readline()
    input = input.strip().split(',')
for i in range(10**9):
    if ''.join(line) in seen:
        break
    seen.add(''.join(line))
    dance(input)
line=[chr(x) for x in range(ord('a'), ord(letter)+1)]
for i in range(int(10**9%len(seen))):
    dance(input)
print ("Answer:",''.join(line))
