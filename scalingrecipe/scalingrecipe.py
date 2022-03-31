from functools import reduce
from math import gcd, ceil

n, x, y = map(int, input().split())
ns = [int(input()) for _ in range(n)]
d = reduce(gcd, ns[1:], ns[0])
scale = ceil(y / (x / d))
ns = [(i // d) * scale for i in ns]

print(*ns, sep="\n")
