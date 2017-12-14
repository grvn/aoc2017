#!/usr/bin/env python3

import sys

filename = sys.argv[1]
severity = 0
delay = 0
caught = True

with open(filename) as f:
    input = f.readlines()
    input = [list(map(int,line.split(":"))) for line in input]
while(caught):
    caught=False
    for d, r in input:
        if ((delay+d) % ((r-1)*2)) == 0:
            delay+=1
            caught=True
            break
print (delay)
