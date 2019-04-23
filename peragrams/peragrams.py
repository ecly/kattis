from collections import Counter
print(max(sum(x % 2 for x in Counter(input()).values()) - 1, 0))
