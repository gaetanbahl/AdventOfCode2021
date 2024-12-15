from collections import defaultdict

map_ = defaultdict(int)

def draw(xs, ys, xe, ye, map_):
    xc, yc = xs, ys
    if xs > xe:
        dx = -1
    else:
        dx = 1

    if ys > ye:
        dy = -1
    else:
        dy = 1

    map_[(xc, yc)] += 1

    done = False
    while not done:
        xc = xc + (xc != xe) * dx
        yc = yc + (yc != ye) * dy
        map_[(xc, yc)] += 1

        done = (xc == xe) and (yc == ye)


with open("input.txt") as f:
    while (line := f.readline()) != "":
        line = line.strip()
        start, end = line.split("->")

        xs, ys = [int(x.strip()) for x in start.split(",")]
        xe, ye = [int(x.strip()) for x in end.split(",")]

        draw(xs, ys, xe, ye, map_)


    count_overlap = 0
    for v in map_.values():
        count_overlap += (v > 1)

    print(count_overlap)
