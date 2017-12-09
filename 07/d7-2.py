import sys
import re

root = set()
leaf = set()
nodes = {}

class Node:
    def __init__(self,name,weight,kids):
        self.name=name
        self.weight=weight
        self.kids=kids

def calculate_weight(x):
    if not nodes[x].kids:
        return nodes[x].weight
    else:
        return sum([calculate_weight(y) for y in nodes[x].kids]) + nodes[x].weight

filename = sys.argv[1];
regex = re.compile(r'^(\w+)\s+\((\d+)\)\s*-?>?\s?([A-Za-z, ]*)')
regex2 = re.compile(r'\W+')
with open(filename) as f:
    for line in f:
        root.add(line.split(' ')[0])
        leaf.update(re.findall(r'\b\w+(?=[,\n])',line))
        input = regex.match(line)
        nodes[input.group(1)] = Node(input.group(1),int(input.group(2)),regex2.split(input.group(3)))
        if nodes[input.group(1)].kids == ['']:
            nodes[input.group(1)].kids = []

tovisit = root - leaf

while tovisit:
    node = tovisit.pop()
    weights = [calculate_weight(x) for x in nodes[node].kids]
    if len(set(weights))>1:
        v1 = min(weights, key=weights.count)
        v2 = max(weights, key=weights.count)
        tovisit.add(nodes[node].kids[weights.index(v1)])
    
print "Answer:",nodes[node].name,nodes[node].weight+(v2-v1)
