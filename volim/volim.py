k = int(input())
n = int(input())
index = k - 1
total_time = 0
for _ in range(n):
    time, answer = input().split()
    total_time += int(time)
    if total_time >= 210:
        break

    if answer == "T":
        index = (index + 1) % 8

print(index + 1)
