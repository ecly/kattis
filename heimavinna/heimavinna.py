ranges = input().split(";")
n = 0
for range in ranges:
    ns = [int(r) for r in range.split("-")]
    n += ns[1] - ns[0] + 1 if len(ns) > 1 else 1

print(n)
