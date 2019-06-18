A, B, C, D = map(int, input().split())
for i in map(lambda x: int(x) - 1, input().split()):
    count = 0

    i1 = i % (A + B)
    if i1 < A:
        count += 1

    i2 = i % (C + D)
    if i2 < C:
        count += 1

    if count == 0:
        print("none")
    if count == 1:
        print("one")
    if count == 2:
        print("both")
