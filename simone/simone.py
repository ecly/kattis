from collections import Counter
from itertools import takewhile

n, k = map(int, input().split())
counter = Counter({k: 0 for k in range(1, k + 1)})
counter.update(map(int, input().split()))
counts = counter.most_common()
lowest_frequency = counts[-1][1]
least_frequent = list(takewhile(lambda c: c[1] <= lowest_frequency, counts[::-1]))
print(len(least_frequent))
print(*sorted([e for e, _ in least_frequent]))
