n = int(input())
ts = list(map(int, input().split()))
idx, temps = min(enumerate(zip(ts, ts[2:]), 1), key=lambda x: max(x[1]))
print(idx, max(temps))
