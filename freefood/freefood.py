n = int(input())
days = set()
for _ in range(n):
    s, t = list(map(int, input().split()))
    for d in range(s, t + 1):
        days.add(d)

print(len(days))
