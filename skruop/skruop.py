n = int(input())
v = 7
for _ in range(n):
    dv = 1 if "op" in input() else -1
    v = min(10, max(0, dv + v))

print(v)
