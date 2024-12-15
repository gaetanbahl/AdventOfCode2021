with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

opening = ['{', '[', '(', '<']
closing = ['}', ']', ')', '>']
scores =  {'}':1197,']':57,')':3,'>':25137}

score = 0
for l in lines:

    stack = []
    for car in l:

        if car in opening:
            stack.append(car)
        elif car in closing:
            if stack[-1] == opening[closing.index(car)]:
                stack.pop()
            else:
                score += scores[car]
                break

print(score)

