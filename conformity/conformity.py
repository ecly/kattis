from collections import Counter

n = int(input())
x = []
for _ in range(n):
    x.append(tuple(sorted(map(int, input().split()))))

counts = Counter(x).most_common()
most_popular_count = counts[0][1]
result = 0
for _, c in counts:
    if c >= most_popular_count:
        result += c

print(result)
