import numpy as np

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

crabs = np.array([int(x) for x in lines[0].split(",")])
dist = np.abs(crabs - np.round(np.mean(crabs))+1)
print(np.sum(dist*(dist+1)/2))
