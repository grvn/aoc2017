import sys
import re

root = set()
leaf = set()
filename = sys.argv[1];
with open(filename) as f:
    for line in f:
            root.add(line.split(' ')[0])
            leaf.update(re.findall(r'\b\w+(?=[,\n])',line))


print "Answer: ", root - leaf
