n = int(input())
intervals = []
for _ in range(n):
    s, f = map(int, input().split())
    intervals.append((s, f))

intervals = sorted(intervals, key=lambda x: x[1])
end = 0
count = 0
for s, f in intervals:
    if s >= end:
        count += 1
        end = f

print(count)
