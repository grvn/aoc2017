#!/usr/bin/env python3

from sys import argv
from re import findall

filename=argv[1]
hit=0
oldhit=0
wait=0

with open(filename) as f:
    input = f.readlines()
    input = [[int(x) for x in findall("[-\d]+", line)] for line in input]
while True:
    for prtcl in input:
        prtcl[3]+=prtcl[6]
        prtcl[4]+=prtcl[7]
        prtcl[5]+=prtcl[8]
        prtcl[0]+=prtcl[3]
        prtcl[1]+=prtcl[4]
        prtcl[2]+=prtcl[5]
    p=[(x[0],x[1],x[2]) for x in input]
    input=[input[index] for index,val in enumerate(p) if p.count(val)==1]
    hit=len(input)
    if hit==oldhit:
        wait+=1
    if wait>=1000:
        break
    oldhit=hit
print("Answer:",len(input))
