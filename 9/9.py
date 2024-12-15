with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

mat = []
for l in lines:
    mat.append([])
    mat[-1] = [int(x) for x in l]

def neigh(i,j,m):

    h, w = len(m), len(m[0])

    neigh = []
    if i == 0:
        neigh.append(m[i+1][j])
    elif i == h-1:
        neigh.append(m[i-1][j])
    else:
        neigh.append(m[i-1][j])
        neigh.append(m[i+1][j])

    if j == 0:
        neigh.append(m[i][j+1])
    elif j == h-1:
        neigh.append(m[i][j-1])
    else:
        neigh.append(m[i][j+1])
        neigh.append(m[i][j-1])

    return neigh

s = 0 
for i in range(len(lines)):
    for j in range(len(lines[0])):

        if mat[i][j] < min(neigh(i,j,mat)):
            s += 1 + mat[i][j]

print(s)



