_n = int(input())
ws = list(map(int, input().split()))
print("yes" if sum(ws) % 3 == 0 else "no")
