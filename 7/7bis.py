import numpy as np
from tqdm import trange
import matplotlib.pyplot as plt

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

crabs = np.array([int(x) for x in lines[0].split(",")])

minc = np.min(crabs)
maxc = np.max(crabs)

min_fuel = np.inf
fuels = []
for i in range(minc, maxc+1):

    dists = np.abs(crabs - i)
    fuel = np.sum(dists*(dists+1)/2)
    min_fuel = min_fuel if min_fuel < fuel else fuel
    fuels.append(fuel)

print(min_fuel)

plt.plot(fuels)
plt.show()
    
