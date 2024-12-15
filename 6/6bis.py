from collections import defaultdict
import time

with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

fish = lines[0].split(",")
fishbuckets = defaultdict(int)
for f in fish:
    fishbuckets[int(f)] += 1

start = time.time()
for d in range(256):
    new_buckets = defaultdict(int)
    new_buckets[8] = fishbuckets[0]
    for b in fishbuckets:
        new_buckets[b-1 if b > 0 else 6] += fishbuckets[b]

    fishbuckets = new_buckets
print(time.time() - start)

print(sum(fishbuckets.values()))

