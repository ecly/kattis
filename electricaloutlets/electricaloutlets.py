n = int(input())
for _ in range(n):
    k, *ns = [int(i) for i in input().split()]
    print(sum(ns) - k + 1)
