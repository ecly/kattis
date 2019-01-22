N, P, Q = map(int, input().split())
if int((P + Q) / N) % 2 == 0:
    print("paul")
else:
    print("opponent")
