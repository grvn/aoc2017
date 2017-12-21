#!/usr/bin/env python3

import sys

filename=sys.argv[1]
iterations=int(sys.argv[2])
rules={}
start=((".", "#", "."), (".", ".", "#"), ("#", "#", "#"))

def rotate(sqgr): 
    return tuple(tuple(x) for x in zip(*sqgr[::-1]))

with open(filename) as f:
    input = f.readlines()
    input = [line.strip() for line in input]
for line in input:
    fro,to=line.split(' => ')
    fro=tuple(map(tuple, fro.split('/')))
    to=tuple(map(tuple, to.split('/')))
    fro0=fro
    while True:
        rules[fro]=to
        fro=rotate(fro)
        if fro==fro0:
            break
    fro=tuple(reversed(fro))
    fro0=fro
    while True:
        rules[fro]=to
        fro=rotate(fro)
        if fro==fro0:
            break
for i in range(iterations):
    size=len(start)
    if size%2==0:
        rwlen=2
    else:
        rwlen=3
    tmp=(size//rwlen)*(rwlen+1)
    tmplist=[[0 for _ in range(tmp)] for _ in range(tmp)]
    for j in range(0,size,rwlen):
        for k in range(0,size,rwlen):
            if rwlen==2:
                keytup=((start[j][k],start[j][k+1]),(start[j+1][k],start[j+1][k+1]))
            else:
                keytup=((start[j][k],start[j][k+1],start[j][k+2]),(start[j+1][k],start[j+1][k+1],start[j+1][k+2]),(start[j+2][k],start[j+2][k+1],start[j+2][k+2]))
            newpart=rules[keytup]
            offsetx=(j//rwlen)*(rwlen+1)
            offsety=(k//rwlen)*(rwlen+1)
            for l in range(rwlen+1):
                for m in range(rwlen+1):
                    tmplist[offsetx+l][offsety+m]=newpart[l][m]
    start=tuple(tuple(z) for z in tmplist)
print(sum(line.count('#') for line in start))
