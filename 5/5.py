from collections import defaultdict

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

lines = [l.split(" -> ") for l in lines if l != '']

vents = defaultdict(lambda :0)

n_double = 0
for l in lines:
    start, end = l[0].split(","), l[1].split(",")
    start = int(start[0]), int(start[1])
    end = int(end[0]), int(end[1])

    id_it, id_eq = [int(start[i] == end[i]) for i in [0,1]]
   
    if not 1 in (id_it, id_eq):
        continue

    first, last = sorted([start[id_it], end[id_it]])

    for i in range(first, last+1):
        vent = [0, 0]
        vent[id_it] = i
        vent[id_eq] = start[id_eq]
        vent = tuple(vent)
        vents[vent] += 1
        if vents[vent] == 2:
            n_double += 1

print(n_double)
        
