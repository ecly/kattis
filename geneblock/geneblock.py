t = int(input())
for _ in range(t):
    n = int(input())
    rem = n % 10
    minimum = 0
    for _ in range(10):
        rem = rem + 3 if rem < 7 else rem % 7
        minimum += 1
        if rem == 0:
            break

    if n / 7 < minimum:
        print(-1)
    else:
        print(minimum)
