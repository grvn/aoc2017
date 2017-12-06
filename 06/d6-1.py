import sys

filename = sys.argv[1];
with open(filename) as f:
    input = f.readline()
    input = [int(x) for x in input.split()]

seen = set()
while str(input) not in seen:
    seen.add(str(input))
    high = max(input)
    index = input.index(high)
    input[index] = 0
    for k in range(high):
        input[(index+k+1)%len(input)] += 1
        
print "Answer: ", len(seen)
