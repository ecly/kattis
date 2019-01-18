N, M = list(map(int, input().split()))
remaining = M - N
piece = "piece" if abs(remaining) == 1 else "pieces"
if remaining >= 0:
    print("Dr. Chaz will have %d %s of chicken left over!" % (remaining, piece))
else:
    print("Dr. Chaz needs %d more %s of chicken!" % (abs(remaining), piece))
