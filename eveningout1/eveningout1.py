a, b = map(int, input().split())
m = a % b
print(min(m, b-m))
