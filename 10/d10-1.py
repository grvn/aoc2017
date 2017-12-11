import sys

def revList(lst,start,howmany):
    howmany = start+howmany-1
    while start <= howmany:
        lst[start % size], lst[howmany % size] = lst[howmany % size], lst[start % size]
        start+=1
        howmany-=1
    return lst

filename = sys.argv[1]
size = int(sys.argv[2])

with open(filename) as f:
    input = f.readline()
    input = [int(x) for x in input.split(",")]
thelist = range(size)

pos=0
skip=0

for value in input:
    revList(thelist,pos,value)
    pos = pos+skip+value%size
    skip = (skip+1)%size


print "Answer:", thelist[0]*thelist[1]
