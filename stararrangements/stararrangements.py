s = int(input())
print("%d:" % s)
for i in range(2, s // 2 + 2):
    if s % (i * 2 - 1) == 0 or (s - i) % (i * 2 - 1) == 0:
        print("%d,%d" % (i, i - 1))
    if s % i == 0:
        print("%d,%d" % (i, i))
