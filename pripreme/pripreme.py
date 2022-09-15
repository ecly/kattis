n = int(input())
ns = sorted(map(int, input().split()))
if n == 1:
    print(ns[0] * 2)
else:
    slowest = ns[-1]
    sum_of_rest = sum(ns[:-1])
    print(sum_of_rest + slowest + max(slowest - sum_of_rest, 0))
