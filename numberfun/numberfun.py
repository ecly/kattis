N = int(input())
for _ in range(N):
    a, b, c = list(map(int, input().split()))
    if a - b == c or b - a == c or a / b == c or b / a == c or a + b == c or a * b == c:
        print("Possible")
    else:
        print("Impossible")
