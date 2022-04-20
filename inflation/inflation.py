from statistics import mean
n = int(input())
canisters = sorted(list(map(int, input().split())))
balloons = list(range(1, n+1))

f = 1

for b, c in zip(balloons, canisters):
    if b < c:
        print("impossible")
        break

    f = min(f, c/b)
else:
    print(f)
