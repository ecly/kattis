from collections import defaultdict
n = int(input())
slats = defaultdict(int)
for _ in range(n):
    for pos, state in zip("TTLL", input()):
        if state == "0":
            slats[pos] += 1

t, l = slats["T"], slats["L"]
swords = min(t, l) // 2
used_slats = swords * 2
t_left, l_left = t - used_slats, l - used_slats

print(swords, t_left, l_left)
