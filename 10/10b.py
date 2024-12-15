import numpy as np

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

opening = ['{', '[', '(', '<']
closing = ['}', ']', ')', '>']
scores =  {'{':3,'[':2,'(':1,'<':4}

s = []
for l in lines:

    stack = []
    error = False
    for car in l:

        if car in opening:
            stack.append(car)
        elif car in closing:
            if stack[-1] == opening[closing.index(car)]:
                stack.pop(-1)
            else:
                error = True
                break
    if not error:
        l_score = 0

        while stack:
            car = stack.pop(-1)
            l_score *= 5
            l_score += scores[car]

        s.append(l_score)

print(int(np.median(s)))

