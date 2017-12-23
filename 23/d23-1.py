#!/usr/bin/env python3

from sys import argv
from collections import defaultdict

filename=argv[1]
count=0
reg=defaultdict(lambda:0)
pos=0

with open(filename) as f:
    input = f.readlines()
    input = [line.split() for line in input]

def exec(reg, val):
    try:
        int(val)
        return int(val)
    except ValueError:
        return reg[val]
    
while pos>=0 and pos<len(input)-1:
    ins = input[pos]
    if ins[0]=='set':
        reg[ins[1]]=exec(reg,ins[2])
    elif ins[0]=='sub':
        reg[ins[1]]-=exec(reg,ins[2])
    elif ins[0]=='mul':
        reg[ins[1]]*=exec(reg,ins[2])
        count+=1
    elif ins[0]=='jnz':
        if exec(reg,ins[1]) != 0:
            pos+=exec(reg,ins[2])
            continue
    pos+=1
print ("Answer:",count)
