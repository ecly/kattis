import fileinput
for line in fileinput.input():
    n = int(line)
    if n < 3:
        print(n)
    else:
        print((n - 1) * 2)
