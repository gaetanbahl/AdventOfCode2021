from tqdm import trange

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

fish = [int(x) for x in lines[0].split(",")]

days = 80

for d in trange(days):
    new_fish = fish[:]
    for i,f in enumerate(fish):
       new_fish[i] = f-1 if f > 0 else 6 
       if f == 0:
           new_fish.append(8)
    fish = new_fish

print(len(fish)) 
