h, m = [int(x) for x in input().split()]

if m - 45 < 0:
    h -= 1
    if h < 0:
        h = 23
    m = 60 - abs(m-45)
else:
    m = m - 45

print(h, m)
