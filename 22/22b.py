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

def point_in_cube(p, c):
    if p[0] < c[3] and p[0] > c[0]:
        if p[1] < c[4] and p[1] > c[1]:
            if p[2] < c[5] and p[2] > c[2]:
                return True
    return False

def are_intersecting(c1,c2):

    cubes = [c1, c2]
    for i,c in enumerate(cubes):
        for x in [c1[0], c1[3]]:
            for y in [c1[1], c1[4]]:
                for z in [c1[2], c1[5]]:
                    if point_in_cube((x,y,z), c):
                        return True
    return False


def intersection(c1,c2):
    if not are_intersecting(c1, c2): 
        return None


engine = defaultdict(int)

parsed = list(map(parse_line, lines))

p = index.Property()
p.dimension = 3
index = index.Index(properties=p)

for i,p in enumerate(parsed[:20]):
   
    inter = index.intersection(p, objects=True)

    index.insert(i, p[1], obj=p[0])
