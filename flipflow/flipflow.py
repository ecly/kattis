t, s, n = map(int, input().split())
ns = list(map(int, input().split()))

m = 1
lower_grams = s
for prev_t, curr_t in zip(ns + [t], ns[1:] + [t]):
    dt = curr_t - prev_t
    lower_grams = min(s, max(0, lower_grams - dt * m))
    m *= -1

print(s - lower_grams if m == 1 else lower_grams)
