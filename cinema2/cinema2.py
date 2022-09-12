n, m = map(int, input().split())
ns = list(map(int, input().split()))
visitors = 0
groups = 0
for group_size in ns:
    visitors += group_size
    if visitors > n:
        break

    groups += 1

print(m - groups)
