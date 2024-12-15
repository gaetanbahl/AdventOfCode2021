import numpy as np
from queue import PriorityQueue

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

array = []
for l in lines:
    row = []
    for c in l:
        row.append(int(c))
    array.append(row)

m = np.array(array, dtype=np.int)
h,w = m.shape

full = np.tile(m, (5,5))

for i in range(5):
    for j in range(5):
        full[i*h:(i+1)*h,j*w:(j+1)*w] += i + j
        full[i*h:(i+1)*h,j*w:(j+1)*w] = np.mod(full[i*h:(i+1)*h,j*w:(j+1)*w]-1, 9) +1

m = full
dist = np.ones(m.shape, dtype=np.int)*np.inf
dist[0,0] = 0

def neigh(p,h,w):
    i,j = p
    neigh = []
    if i != 0:
        neigh.append((i-1,j))
    if i != h-1:
        neigh.append((i+1,j))
    if j != 0:
        neigh.append((i,j-1))
    if j != w-1:
        neigh.append((i,j+1))
    return neigh


h,w = m.shape
q = PriorityQueue()
q.put((0, (0,0)))

visited = set()

while q.qsize() > 0:
    _,u = q.get()
    visited.add(u)

    if u == (h-1,w-1):
        break

    for n in neigh(u,h,w):
        if not n in visited:
            if dist[u] + m[n] < dist[n]:
                dist[n] = dist[u] + m[n]
                q.put((dist[n], n))

print(dist[(h-1,w-1)])
