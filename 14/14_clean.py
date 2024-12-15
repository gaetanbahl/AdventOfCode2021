from collections import deque, defaultdict, Counter

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

start = lines[0]
q = list(start)

rules = dict()
for l in lines[2:]:
    r = l.split(" -> ")
    rules[(r[0][0],r[0][1])] = r[1]

memo = dict() 

def insert_two(fst, snd, rules, d, cnt=0):

    if (fst, snd, cnt) in memo:
        new_d = memo[(fst, snd, cnt)]
        d.update(new_d)
        return

    new_d = Counter()

    if cnt == 0:
        new_d[fst] += 1

    if cnt == 40:
        return

    if (fst, snd) in rules:
        new_car = rules[(fst, snd)]
        new_d[new_car] += 1
        
        insert_two(fst, new_car, rules, new_d, cnt+1)
        insert_two(new_car, snd, rules, new_d, cnt+1)

    d.update(new_d)

    memo[(fst,snd,cnt)] = new_d


def insert_all(q, rules):

    d = Counter()
    
    for i,c in enumerate(q[:-1]):
        insert_two(c, q[i+1], rules, d, 0)

    d[q[-1]] += 1

    return d
    

d = insert_all(q, rules)

print(len(memo.keys()))

counts = sorted(list(d.items()), key= lambda c:c[1])
#print(list(d.items()))
#print(counts[0])
#print(counts[-1])
print(counts[-1][1] - counts[0][1])
