from collections import Counter
N = int(input())
for case in range(1, N+1):
    G = int(input())
    codes = list(map(int, input().split()))
    counter = Counter(codes)
    for k, v in counter.items():
        if v == 1:
            print("Case #%d: %d" % (case, k))
            break
