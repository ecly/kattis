n = int(input())
ns = [int(input()) for _ in range(n)]
print(min(ns[i] + ns[(i+2) % n] for i in range(n)))
