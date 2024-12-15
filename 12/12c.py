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

def dict_to_str(d):
    s = ""
    for k in sorted(d):
        s += (k + str(d[k]))
    return s

def find_paths(graph, curr, visited):

    s = dict_to_str(visited)
    if (curr,s) in memo:
        return memo[(curr,s)]

    d = visited.copy()
    d[curr] += 1

    if curr == "end":
        return 1

    paths = 0
    for nex in graph[curr]:
        if not (nex in smol and d[nex] > 1):
            paths += find_paths(graph, nex, d)

    memo[(curr,dict_to_str(visited))] = paths

    return paths

memo = dict()

visited = defaultdict(int)
visited["start"] = 50

paths = find_paths(graph, "start", visited)
print(paths)

