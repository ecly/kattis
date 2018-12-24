P, N = list(map(int, input().split()))
parts = set()
for i in range(N):
    p = input()
    parts.add(p)
    if len(parts) == P:
        print(i + 1)
        break

if len(parts) < P:
    print("paradox avoided")
