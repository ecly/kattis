ns = [int(input()) for _ in range(int(input()))]
print(1 + sum(a > b for a, b in zip(ns, ns[1:])))
