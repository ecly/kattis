import sys
lengths = list(map(len, sys.stdin.readlines()))
n = max(lengths)
penalties = list(map(lambda l: (n - l) ** 2, lengths))
print(sum(penalties[:-1]))
