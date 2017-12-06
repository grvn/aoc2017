import sys

filename = sys.argv[1];
with open(filename) as f:
    input = f.readlines()
    input = [int(x) for x in input]

i = 0
s = 0
l = list(input)
while i>= 0 and i < len(input):
    s += 1
    lt = l[i]
    if l[i] >= 3:
        l[i] -= 1
    else:
        l[i] += 1
    i += lt
print "Answer:", s
