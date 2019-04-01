import fileinput
for idx, line in enumerate(fileinput.input(), 1):
    numbers = list(map(int, line.split()[1:]))
    lo, hi = min(numbers), max(numbers)
    print("Case %d: %d %d %d" % (idx, lo, hi, hi - lo))
