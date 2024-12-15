import numpy as np

with open("input.txt", 'r') as f:
    lines = [l.strip().split("|") for l in f.readlines()]


n = 0
for l in lines:
    digits = l[1].split(" ")
    for d in digits:
        if len(d) in [2,3,4,7]:
            n+=1
print(n)
