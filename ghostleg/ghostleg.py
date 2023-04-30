n, m = map(int, input().split())
vs = list(range(n))
for _ in range(m):
    a = int(input())
    vs[a - 1], vs[a] = vs[a], vs[a - 1]

print("\n".join(str(i + 1) for i in vs))
