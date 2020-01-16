n, p = map(int, input().split())
listeners = list(map(int, input().split()))
best = 0
for i in range(n):
    c = listeners[i]
    if c <= p:
        continue

    profit = c - p
    local_best = profit
    for j in range(i + 1, n):
        profit += listeners[j] - p
        if profit < 0:
            break
        if profit > local_best:
            local_best = profit

    if local_best > best:
        best = local_best

print(best)
