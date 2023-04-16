import fileinput
from collections import Counter

counts = Counter(line.strip() for line in fileinput.input())
population = sum(counts.values())
for k, v in sorted(counts.items()):
    print(k, v / population * 100)
