import sys

filename = sys.argv[1];
with open(filename) as f:
    input = f.readline()
    input = [int(x) for x in input.split()]

def main(find):
    seen = set()
    seen.add(str(find))
    while True:
        seen.add(str(input))
        high = max(input)
        index = input.index(high)
        input[index] = 0
        for k in range(high):
            input[(index+k+1)%len(input)] += 1
        if str(input) in seen:
            break
    return str(input), len(seen)

find, _ = main(input)
print "Answer: ", main(find)
