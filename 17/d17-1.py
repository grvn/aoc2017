#!/usr/bin/env python3

import sys

step=int(sys.argv[1])
steps=int(sys.argv[2])
buffer=[0]
current=0

for i in range(1,steps+1):
    current=((current+step)%i)+1
    buffer=buffer[:current]+[i]+buffer[current:]
    current=buffer.index(i)
print ("Answer:",buffer[current+1%len(buffer)])
