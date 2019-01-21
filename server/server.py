n, T = map(int, input().split())
tasks = map(int, input().split())
count = 0
total = 0
for task in tasks:
    if total + task <= T:
        total += task
        count += 1
    else:
        break

print(count)
