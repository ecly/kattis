import sys
from collections import Counter
counts = Counter(sys.stdin.readlines()[:-1])
candidates = counts.most_common(2)
if candidates[0][1] == candidates[1][1]:
    print("Runoff!")
else:
    print(candidates[0][0].strip())
