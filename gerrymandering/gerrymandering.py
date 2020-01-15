p, d = map(int, input().split())
dic = {}
for _ in range(1, p + 1):
    di, a, b = map(int, input().split())
    ca, cb = dic.get(di, (0, 0))
    dic[di] = (ca + a, cb + b)

wa, wb, v = 0, 0, 0
for di in sorted(dic):
    a, b = dic[di]
    threshold = (a + b) // 2
    winner = "A" if a > b else "B"
    wasted_a = a - threshold - 1 if a > b else a
    wasted_b = b - threshold - 1 if b > a else b
    print(winner, wasted_a, wasted_b)

    wa += wasted_a
    wb += wasted_b
    v += a + b

print(abs(wa - wb) / v)
