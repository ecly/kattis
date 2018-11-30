from collections import defaultdict
cards = [x[0] for x in input().split()]
counter = defaultdict(int)
for c in cards:
    counter[c] += 1

print(max(counter.values()))
