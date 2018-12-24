p = int(input())
for _ in range(p):
    k, n = list(map(int, input().split()))
    count = sum(range(1, n + 1)) + n
    print(k, count)
