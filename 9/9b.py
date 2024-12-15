from tqdm import tqdm

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

mat = []
for l in lines:
    mat.append([])
    mat[-1] = [int(x) for x in l]

def neigh(p,m):

    i,j = p

    h, w = len(m), len(m[0])

    neigh = set()
    if i == 0:
        neigh.add((i+1,j))
    elif i == h-1:
        neigh.add((i-1,j))
    else:
        neigh.add((i-1,j))
        neigh.add((i+1,j))

    if j == 0:
        neigh.add((i,j+1))
    elif j == w-1:
        neigh.add((i,j-1))
    else:
        neigh.add((i,j+1))
        neigh.add((i,j-1))

    return neigh


low_points = []
for i in range(len(lines)):
    for j in range(len(lines[0])):

        if mat[i][j] < min([mat[y][x] for y,x in neigh((i,j),mat)]):
            low_points.append((i,j))

def explore(p,m):

    stack = [p]
    s = set(stack)

    while len(stack) > 0:

        curr = stack.pop()
        n = neigh(curr, m)

        n = list(filter(lambda p : m[p[0]][p[1]] < 9, n))
        stack += list(set(n) - s)
        s.update(n)

    return len(s)


basins = []
for p in low_points:
    basins.append(explore(p,mat))

out = sorted(basins, reverse=True)[0:3]
print(out[0]*out[1]*out[2])
