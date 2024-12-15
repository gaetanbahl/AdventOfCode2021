import numpy as np
from collections import defaultdict
from sortedcontainers import SortedKeyList, SortedList

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

array = []
for l in lines:
    row = []
    for c in l:
        row.append(int(c))
    array.append(row)

m = np.array(array)
m = np.pad(m, 1, constant_values=np.inf)
h,w = m.shape

dist = np.ones(m.shape)*np.inf

def neigh(p):
    i,j = p
    return [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]

dist[1,1] = 0

q = [(i,j) for i in range(1,w-1) for j in range(1,h-1)]

while q:
    u = (sorted(q, key=lambda x : -dist[x])).pop()
    q.remove(u)

    if u == (h-2,w-2):
        break

    for n in neigh(u):
        if n in q:
            if dist[u] + m[n] < dist[n]:
                dist[n] = dist[u] + m[n]

print(dist)
print(dist[(h-2,w-2)])
