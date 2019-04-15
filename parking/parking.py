prices = [0] + list(map(int, input().split()))
parked = [0 for i in range(100)]
for _ in range(3):
    x, y = map(lambda x: int(x) - 1, input().split())
    for i in range(x, y):
        parked[i] += 1

print(sum(map(lambda p: prices[p] * p, parked)))
