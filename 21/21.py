with open("input.txt", 'r') as f:
    positions = [int(l.strip().split(": ")[1]) for l in f.readlines()]


positions = [p-1 for p in positions]

scores = [0,0]

def die():
    n = 1
    while True:
        yield n
        n += 1
        if n == 101:
            n = 1

d = die()

nrolls = 0
while max(scores) < 1000:
    for i in range(2):
        total = 0
        for _ in range(3):
            total +=  next(d)
            nrolls += 1

        positions[i] += total
        positions[i] = positions[i] % 10
        scores[i] += positions[i] +1

print(scores)

print(min(scores) * nrolls)
        
    

