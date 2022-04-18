from itertools import takewhile

n, dm = map(int, input().split())
ds = map(int, input().split())
years = len(list(takewhile(lambda i: i > dm, ds)))
print(
    f"It hadn't snowed this early in {years} years!"
    if years < n
    else "It had never snowed this early!"
)
