_n = int(input())
ns = sorted(list(map(int, input().split())))
print(ns[0] * (len(ns) - 1) + sum(ns[1:]))
