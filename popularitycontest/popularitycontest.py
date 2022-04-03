n, m = map(int, input().split())
f = {i + 1: 0 for i in range(n)}
for i in range(m):
    a, b = map(int, input().split())
    f[a] += 1
    f[b] += 1

print(*[p - s for s, p in f.items()])
