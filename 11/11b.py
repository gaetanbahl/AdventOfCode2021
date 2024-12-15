with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

mat = []
for l in lines:
    mat.append([])
    mat[-1] = [int(x) for x in l]

def point_in_mat(i,j,h,w):
    return i>= 0 and j>=0 and i < h and j < w

def neigh(p,m):

    i,j = p

    h, w = len(m), len(m[0])

    neigh = set()
    for pi in range(i-1,i+2):
        for pj in range(j-1,j+2):
            if point_in_mat(pi,pj,h,w):
                neigh.add((pi,pj))

    return neigh

def step(m):
    flash = set()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            m[i][j] += 1
            if m[i][j] > 9:
                flash.add((i,j))

    stack = list(flash)
    while stack:
        p = stack.pop()
        neighs = neigh(p,m)
        for n in neighs:
            i,j = n
            m[i][j] += 1
            if m[i][j] > 9 and not (i,j) in flash:
                flash.add((i,j))
                stack.append((i,j))

    for i,j in flash:
        m[i][j] = 0

    return len(flash)

s = 0
while True:
    s += 1
    if step(mat) == len(mat) * len(mat[0]):
        break

print(s)



