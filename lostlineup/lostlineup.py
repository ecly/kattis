from operator import itemgetter

n = int(input())
diffs = map(int, input().split())
line = [1]
line.extend(map(itemgetter(0), sorted(enumerate(diffs, 2), key=itemgetter(1))))
print(" ".join(map(str, line)))
