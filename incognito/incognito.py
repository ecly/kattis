import sys
from collections import defaultdict

def disguise_count(case):
    count = 1
    for i in list(case.values()):
        count *= len(i) + 1

    return count-1

lines = sys.stdin.readlines()
cases = []
for line in lines[1:]:
    if line.strip().isdigit():
        cases.append(defaultdict(list))
        continue

    name, category = line.strip().split()
    cases[-1][category].append(name)

for case in cases:
    print(disguise_count(case))
