#!/usr/bin/env python3

import sys

step=int(sys.argv[1])
steps=int(sys.argv[2])
answer=0
current=0

for i in range(1,steps+1):
    current=((current+step)%i)
    if current==0:
        answer=i
    current+=1
print ("Answer:",answer)
