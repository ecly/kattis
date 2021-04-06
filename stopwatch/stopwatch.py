n = int(input())
if n % 2 == 1:
    print("still running")
else:
    ns = [int(input()) for _ in range(n)]
    print(sum(y - x for x, y in list(zip(ns, ns[1:]))[::2]))
