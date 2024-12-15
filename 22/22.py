from collections import defaultdict
from tqdm import trange
from rtree import index

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]


def parse_coord(s):
    spl = s.split("=")[1].split("..")
    return (int(spl[0]), int(spl[1]))

def parse_line(l):
    space_splt = l.split(" ")

    on_off = 1 if space_splt[0] == "on" else 0

    x,y,z = [parse_coord(s) for s in space_splt[1].split(",")]

    return (on_off, (x[0],y[0],z[0],x[1],y[1],z[1]))

engine = defaultdict(int)

parsed = list(map(parse_line, lines))

p = index.Property()
p.dimension = 3
index = index.Index(properties=p)

for i,p in enumerate(parsed[:20]):
   
    index.insert(i, p[1], obj=p[0])

b = [int(x) for x in index.bounds]

total = 0
for x in trange(-50,51):
    for y in range(-50,51):
        for z in range(-50,51):
            inter = index.intersection((x,y,z,x,y,z), objects=True)

            inter = sorted(inter, key=lambda x : x.id)
            if len(inter) > 0:
                total += inter[-1].object

print(total)


