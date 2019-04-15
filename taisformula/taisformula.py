n = int(input())
t, v = map(float, input().split())
area = 0
for _ in range(n - 1):
    new_t, new_v = map(float, input().split())
    area += (v + new_v) / 2 * (new_t - t)
    t, v = new_t, new_v

print(area / 1000)
