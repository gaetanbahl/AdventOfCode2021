from collections import defaultdict

data = [line.split("-") for line in open("input.txt").read().split()]    

graph = defaultdict(set)
for a, b in data:
    graph[a].add(b)
    graph[b].add(a)

def count_paths(trail, can_repeat):
    if trail[-1] == "end": return 1

    paths = 0
    for next_loc in graph[trail[-1]]:
        if not (next_loc.islower() and next_loc in trail):
            paths += count_paths(trail + (next_loc, ), can_repeat)
        elif can_repeat and trail.count(next_loc) == 1 and next_loc != "start":
            paths += count_paths(trail + (next_loc, ), False)
    return paths

print("1:", count_paths(("start",), False))
print("2:", count_paths(("start",), True))
