a, b, c, n = map(int, input().split())
if a > 0 and b > 0 and c > 0 and a + b + c >= n and n >= 3:
    print("YES")
else:
    print("NO")
