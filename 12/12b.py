from collections import defaultdict, deque

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

graph = defaultdict(set)
smol = set()

for l in lines:
    li = l.split('-')
    start = li[0]
    end = li[1]

    for n in [start, end]:
        if n.lower() == n:
            smol.add(n)

    graph[start].add(end)
    graph[end].add(start)

exploration = [["start"]]
paths = 0

while exploration:

    path = exploration.pop()
    curr = path[-1]

    for nex in graph[curr]:
        if nex == "end":
            paths += 1
            continue
        if not (nex in smol and path.count(nex) > 1 ) and nex != "start":
            exploration.append(path + [nex])

print(paths)
