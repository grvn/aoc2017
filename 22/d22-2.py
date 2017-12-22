#!/usr/bin/env python3

from sys import argv

filename=argv[1]
iters=int(argv[2])
count=0

with open(filename) as f:
    input = f.readlines()
    input = [list(line.strip()) for line in input]
rows=len(input)
cols=len(input[0])
x=rows//2
y=cols//2
input=list(zip(*reversed(input)))
nodes={(a-x,b-y): 0 if input[a][b]=='.' else 1 for a in range(rows) for b in range(cols)}
x=0
y=0
dir=(0,1)
for _ in range(iters):
    if (x,y) in nodes and nodes[(x,y)]!=0:
        if nodes[(x,y)]==1:#infected
            dir=(dir[1],-dir[0])
            nodes[(x,y)]=2
        elif nodes[(x,y)]==2:#flag
            dir=(-dir[0],-dir[1])
            nodes[(x,y)]=0
        elif nodes[(x,y)]==3:#weak
            nodes[(x,y)]=1
            count+=1
    else:#clean
        dir=(-dir[1],dir[0])
        nodes[(x,y)]=3
    x=dir[0]+x
    y=dir[1]+y
print("Answer:",count)
