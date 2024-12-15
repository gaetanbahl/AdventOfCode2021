from collections import defaultdict


with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

graph = defaultdict(set)

for l in lines:
    li = l.split('-')
    start = li[0]
    end = li[1]

    graph[start].add(end)
    graph[end].add(start)

def find_paths(graph, path, can_repeat):

    if path[-1] == "end":
        return 1

    p = 0
    for nex in graph[path[-1]]:
        if nex == "start":
            continue

        if not (nex.islower() and path.count(nex) > 0):
            p += find_paths(graph, path + (nex,), can_repeat)
        if can_repeat:
            if nex.islower() and path.count(nex) == 1:
                p += find_paths(graph, path + (nex,), False)


    return p

paths = find_paths(graph, ("start",), True)
print(paths)

