n = int(input())
def rec(i):
    if i == n:
        return 1
    if i > n:
        return 0

    return rec(i + 1) + rec(i + 2) + rec(i + 3)

print(rec(0))
