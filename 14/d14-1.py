#!/usr/bin/env python3

import sys
from d10_2_rev import knot_hash

filename=sys.argv[1]
squares=0
with open(filename) as f:
    input = f.readline()
    input = input.strip()
for i in range(128):
    row = input+"-"+str(i)
    squares += sum(['{0:08b}'.format(int(x, 16)).count('1') for x in knot_hash(row)])
print ("Answer:",squares)
