s, n = map(int, input().split())
a = set(map(int, input().split()))

added = 0
for i in range(1, s + 1):
    l = i - 1 if i > 1 else s
    r = i + 1 if i < s else 1
    if all(x not in a for x in (i, l, r)):
        a.add(i)
        added += 1

print(added)
