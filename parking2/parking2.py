t = int(input())
for _ in range(t):
    n = input()
    x = sorted([int(i) for i in input().strip().split()])
    print(abs(x[0] - x[-1]) * 2)
