import sys
file = sys.stdin.read()
d, input_ = file.split("\n\n")
d = {b: a for a, b in map(lambda e: e.strip().split(), d.splitlines())}
for line in input_.splitlines():
    print(d.get(line.strip(), "eh"))
