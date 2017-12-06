import sys

filename = sys.argv[1];
with open(filename) as f:
    input = f.readlines()
    input = [int(x) for x in input]

i = 0
s = 0
l = list(input)
while i>=0 and i < len(input):
    s += 1
    l[i] += 1
    i += l[i]-1
print "Answer:", s
