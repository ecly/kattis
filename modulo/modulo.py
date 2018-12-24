import fileinput
print(len({int(x) % 42 for x in fileinput.input()}))
