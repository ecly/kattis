from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    toys = defaultdict(int)
    for _ in range(n):
        toy, count = input().split()
        toys[toy] += int(count)

    print(len(toys))
    for toy, count in sorted(toys.items(), key=lambda t: (-t[1], t[0])):
        print(toy, count)
