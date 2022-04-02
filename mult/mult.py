n = int(input())
first = 0
for _ in range(n):
    n = int(input())
    if not first:
        first = n
    elif n % first == 0:
        print(n)
        first = 0
