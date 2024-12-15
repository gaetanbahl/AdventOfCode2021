from collections import deque, defaultdict
from tqdm import trange, tqdm

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

start = lines[0]

rules = dict()
for l in lines[2:]:
    r = l.split(" -> ")
    rules[r[0]] = r[1]

q = []
for c in start:
    q.append(c)


def insert(q, rules):

    if len(q) == 1:
        return q

    c = q.popleft()
    new_q = insert(q.copy(), rules)
    for r in rules:
        if r[0][0] == c and q[0] == r[0][1]:
            new_q.appendleft(r[1])
            new_q.appendleft(c)
            return new_q
    new_q.appendleft(c)
    return new_q


def insert_it(q, rules):

    new_q = []
    for i,c in enumerate(q[:-1]):
        new_q.append(c)
        k = "".join(q[i:i+2])
        if k in rules:
            new_q.append(rules[k])
    new_q.append(q[-1])

    return new_q


memo = dict() 


def insert_two(first, last, rules, dic, cnt=0):

    if (first,last,cnt) in memo:
        new_dic = memo[(first, last, cnt)]
        for k in new_dic:
            dic[k] += new_dic[k]
        return


    new_dic = defaultdict(int)

    if cnt == 0:
        new_dic[first] += 1

    if cnt == 40:
        return

    s = "".join((first, last))
    if s in rules:
        new_car = rules[s]
        new_dic[new_car] += 1
        
        insert_two(first, new_car, rules, new_dic, cnt+1)
        insert_two(new_car, last, rules, new_dic, cnt+1)

    for k in new_dic:
        dic[k] += new_dic[k]

    memo[(first,last,cnt)] = new_dic


def insert_gneu(q, rules):

    d = defaultdict(int)
    
    for i,c in enumerate(tqdm(q[:-1])):
        insert_two(c, q[i+1], rules, d, 0)

    d[q[-1]] += 1

    return d
    

d = insert_gneu(q, rules)

#print(list(d.items()))

counts = sorted(list(d.items()), key= lambda c:c[1])
#print(counts[0])
#print(counts[-1])
print(counts[-1][1] - counts[0][1])
