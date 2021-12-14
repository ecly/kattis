n = int(input())
m = int(input())
q, r = divmod(m, n)
for _ in range(r):
    print("*" * (q+1))
for _ in range(n - r):
    print("*" * (q))
