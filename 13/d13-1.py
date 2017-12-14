#!/usr/bin/env python3

import sys

filename = sys.argv[1]
severity = 0

with open(filename) as f:
    input = f.readlines()
    input = [list(map(int,line.split(":"))) for line in input]
for d, r in input:
    if (d % ((r-1)*2)) == 0:
        severity+=d*r
print (severity)



# depth = range
#   0   =   x
#   1   =   1
#   2   =  2|1
#   3   =   1
#   4   = 3|2|1
#   5   =   1
#   6   = 4|2|1
#   7   =   1
#   8   = 5|3|2|1
#   9   =   1
#   10  = 6|2|1
#   11  =   1
#   12  = 7|4|3|2|1
