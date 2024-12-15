from collections import defaultdict


with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

graph = defaultdict(list)
smol = set()

for l in lines:
    li = l.split('-')
    start = li[0]
    end = li[1]

    for n in [start, end]:
        if n.lower() == n:
            smol.add(n)

    graph[start].append(end)
    graph[end].append(start)

def find_paths(graph, curr, visited):

    v = visited.copy()
    v.add(curr)

    if curr == "end":
        return [[]]

    paths = []
    for nex in graph[curr]:
        if not (nex in smol and nex in v):
            rest = find_paths(graph, nex, v)
            for np in rest:
                paths.append([nex] + np)

    return paths

paths = find_paths(graph, "start", set())
print(len(paths))

