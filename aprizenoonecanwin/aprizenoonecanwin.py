n, x = map(int, input().split())
ns = sorted(map(int, input().split()))
hi = 0
count = 0
for number in ns:
    if not hi or number + hi <= x:
        count += 1
        hi = number
    else:
        break


print(count)
