n, p, k = map(int, input().split())
ts = list(map(int, input().split()))

speed = 1.0
time_saved = 0
for prev, curr in zip([0] + ts, ts + [k]):
    saved = (curr - prev) * (speed - 1)
    time_saved += saved
    speed += p / 100

print(k + time_saved)
