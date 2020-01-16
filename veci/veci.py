from itertools import permutations
x = int(input())
options = map(lambda i: int("".join(i)), permutations(str(x)))
options = [i for i in options if i > x]
if options:
    print(min(options))
else:
    print(0)
