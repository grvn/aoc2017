#!/usr/bin/env python3

from sys import argv
from re import findall
from math import sqrt
from operator import itemgetter

filename=argv[1]

def pos_min(a):
    val=min(a)
    return [int(ind) for ind, ele in enumerate(a) if val==ele]

with open(filename) as f:
    input = f.readlines()
    input = [[int(x) for x in findall("[-\d]+", line)] for line in input]
a=[sqrt(prtcl[6]**2 + prtcl[7]**2 + prtcl[8]**2) for prtcl in input]
ans=pos_min(a)
if len(ans)>1:
    v=[sqrt(prtcl[3]**2 + prtcl[4]**2 + prtcl[5]**2) for prtcl in itemgetter(*ans)(input)]
    ans=itemgetter(*pos_min(v))(ans)
    if isinstance(ans, tuple):
        p=[sqrt(prtcl[0]**2 + prtcl[1]**2 + prtcl[2]**2) for prtcl in itemgetter(*ans)(input)]
        ans=itemgetter(*pos_min(p))(ans)
print("Answer:",ans)
