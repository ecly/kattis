n, t = map(int, input().split())
durations = sorted([int(input()) for _ in range(n)], reverse=True)

remaining_time = durations.pop(0)
for d in sorted(durations, reverse=True):
    remaining_time -= t
    remaining_time = min(d, remaining_time)

print("YES" if remaining_time > 0 else "NO")
