import sys

def revList(lst,start,howmany):
    howmany = start+howmany-1
    while start <= howmany:
        lst[start % size], lst[howmany % size] = lst[howmany % size], lst[start % size]
        start+=1
        howmany-=1
    return lst

size = 256
def knot_hash(input):
    input = [ord(x) for x in input.strip()]+[17,31,73,47,23]
    thelist = list(range(size))
    pos=0
    skip=0
    for i in range(64):
        for value in input:
            revList(thelist,pos,value)
            pos = pos+skip+value%size
            skip = (skip+1)%size
    dense = []
    for i in range(0, size, 16):
        block = 0
        for j in range(i, i+16):
            block ^= thelist[j]
        dense.append("%02x" % block)
    return dense
