_N = int(input())
print(max(map(sum, (enumerate(sorted(map(int, input().split()), reverse=True), 1)))) + 1)
