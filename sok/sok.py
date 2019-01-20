a, b, c = map(int, input().split())
i, j, k = map(int, input().split())
count = min(a / i, b / j, c / k)
print(a - i * count, b - j * count, c - k * count)
