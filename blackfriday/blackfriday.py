from collections import defaultdict
n = int(input())
counts = defaultdict(int)
numbers = list(map(int, input().split()))
for n in numbers:
    counts[n] += 1

for n in sorted(set(numbers), reverse=True):
    if counts[n] > 1:
        continue
    else:
        print(numbers.index(n) + 1)
        exit(0)

print("none")
