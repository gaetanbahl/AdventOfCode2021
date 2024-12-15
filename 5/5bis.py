from collections import defaultdict

with open("in5.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

lines = [l.split(" -> ") for l in lines if l != '']

vents = defaultdict(int)

n_double = 0
for l in lines:
    start, end = l[0].split(","), l[1].split(",")
    start = int(start[0]), int(start[1])
    end = int(end[0]), int(end[1])
   
    if end[0] == start[0]:
        id_it, id_eq = 1, 0
    elif end[1] == start[1]:
        id_it, id_eq = 0, 1
    else:
        for i in range(abs(end[0]-start[0])+1):
            incrx = 1 if start[0] < end[0] else -1
            incry = 1 if start[1] < end[1] else -1
            vent = (start[0]+incrx*i,start[1]+incry*i)
            vents[vent] += 1
            if vents[vent] == 2:
                n_double += 1
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
        
