s, t, n = map(int, input().split())
d_0, *ds = map(int, input().split())
bs = map(int, input().split())
cs = map(int, input().split())

time = s + d_0
for i, (d, b, c) in enumerate(zip(ds, bs, cs)):
    time += d
    time += time % c
    time += b

print("yes" if time <= t else "no")
