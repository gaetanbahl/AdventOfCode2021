from collections import defaultdict

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

tobin = lambda x: 1 if x == "#" else 0

algorithm = list(map(tobin, lines[0]))

image = defaultdict(int)

for j,l in enumerate(lines[2:]):
    for i,c in enumerate(l):
        image[(i,j)] = tobin(c)

min_i = -2
min_j = -2
max_i = len(lines[2]) +2
max_j = len(lines[2:]) +2

def get(im, x, y):
    out = []
    for j in range(-1,2):
        for i in range(-1,2):
            out.append(str(im[(i+x,j+y)]))

    binstr = "".join(out)

    return int(binstr, 2)

max_it = 50

old_image = image
for it in range(max_it):
    default = (it+1) % 2
    
    new_image = defaultdict(lambda:1 ) if default else defaultdict(int)

    for i in range(min_i, max_i +1):
        for j in range(min_j, max_j +1):
            new_image[(i,j)] = algorithm[get(old_image, i,j)]
#            print(new_image[(i,j)], end="")
#        print()
    old2_image = old_image
    old_image = new_image
    min_i -= 2
    max_i += 2
    min_j -= 2
    max_j += 2

print(sum(old_image.values()))

