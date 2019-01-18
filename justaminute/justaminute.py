N = int(input())
minutes = 0
seconds = 0
for _ in range(N):
    m, s = map(int, input().split())
    minutes += m
    seconds += s

sl_minute = seconds / (minutes * 60)
print("measurement error" if sl_minute <= 1 else sl_minute)
