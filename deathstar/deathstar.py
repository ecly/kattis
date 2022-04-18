from functools import reduce
n = int(input())
m = []
for _ in range(n):
    m.append([int(i) for i in input().split()])

print(*[reduce(lambda a, b: a | b, row, 0) for row in m])
