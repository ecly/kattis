import fileinput
for case, line in enumerate(fileinput.input(), 1):
    e, m = map(int, line.split())
    days = 0
    while e != 0 or m != 0:
        days += 1
        e = (e + 1) % 365
        m = (m + 1) % 687

    print("Case {:d}: {:d}".format(case, days))
