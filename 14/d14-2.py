#!/usr/bin/env python3

import sys
from d10_2_rev import knot_hash

def visit_neigh(point):
    x,y = point
    visited.add(point)
    pos_neigh = [(1,0),(0,1),(-1,0),(0,-1)]
    neigh = [(x+p1,y+p2) for (p1,p2) in pos_neigh if
             (x+p1>=0 and y+p2>=0 and x+p1<length and y+p2<length and grid[x+p1][y+p2] == '1')]
    [visit_neigh(z) for z in neigh if z not in visited]

filename=sys.argv[1]
length=128
grid=[]
visited=set()
regions=0
with open(filename) as f:
    input = f.readline()
    input = input.strip()
for i in range(length):
    row = input+"-"+str(i)
    grid.append([y for y in (''.join(['{0:08b}'.format(int(x, 16)) for x in knot_hash(row)]))])
for i in range(length):
    for j in range(length):
        if grid[i][j] == '1' and (i,j) not in visited:
            visit_neigh((i,j))
            regions+=1
print ("Answer:",regions)
