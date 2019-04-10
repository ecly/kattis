T = int(input())
for i in range(1, T + 1):
    n = int(input())
    v1 = sorted(map(int, input().split()))
    v2 = sorted(map(int, input().split()), reverse=True)
    res = sum(list(map(lambda x: x[0] * x[1], zip(v1, v2))))
    print("Case #%d: %d" % (i, res))
