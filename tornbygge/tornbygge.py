_n = input()
ns = list(map(int, input().split()))
print(sum(y > x for x, y in zip(ns, ns[1:])) + 1)
