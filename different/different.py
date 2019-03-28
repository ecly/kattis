import fileinput
for line in fileinput.input():
    x, y = map(int, line.split())
    print(abs(x - y))
