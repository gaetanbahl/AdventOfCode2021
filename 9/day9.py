with open('in9.txt') as f:
    array = f.readlines()

array = [x.strip() for x in array]


low_points = []
low_points_coords = []

R = len(array)
C = len(array[0])

print(R, C)

# Pad with 9 so I don't have to worry about edges
array = ['9' + x + '9' for x in array]
array = ["".join((C+2) * ['9'])] + array + ["".join((C+2) * ['9'])]

# "Convolve"
for i in range(1, R+1):
    for j in range(1, C+1):
        e = int(array[i][j])

        a = int(array[i-1][j])
        b = int(array[i][j-1])
        c = int(array[i][j+1])
        d = int(array[i+1][j])

        if (e < a) and (e < b) and (e < c) and (e < d):
            low_points.append(e)
            low_points_coords.append((i, j))

print(low_points_coords)
print('Part1:', sum(low_points) + len(low_points))


##### Part 2

from collections import deque

def count_if_unseen(node_value, i, j, q, seen):
    neighbour = int(array[i][j])

    # First check is redundant with the strict inequality in the second
    # but I first wrote it assuming flat areas could be part of basins
    if (neighbour != 9) and (neighbour > node_value) and ((i, j) not in seen):
        q.append((i, j))
        seen.add((i, j))
        return 1
    else:
        return 0

def search_neighbours(i, j, q, seen):
    size = 0
    node_val = int(array[i][j])

    neighbours = [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]
    for (ni, nj) in neighbours:
        size += count_if_unseen(node_val, ni, nj, q, seen)

    return size

def basin_size(i, j):
    # Do a BFS using a queue
    q = deque()
    seen = set()

    size = 1
    seen.add((i,j))
    q.append((i,j))

    while q:
        ni, nj = q.popleft()
        size += search_neighbours(ni, nj, q, seen)

    return size



sizes = []
for lp in low_points_coords:
    size = basin_size(*lp)
    print(lp, size)
    sizes.append(size)

sizes = sorted(sizes)
print(sizes)
print(sizes[-3:])

print("Part 2:", sizes[-3] * sizes[-2] * sizes[-1])