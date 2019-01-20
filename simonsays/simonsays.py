import fileinput
for line in filter(lambda s: s.startswith("Simon says"), fileinput.input()):
    print(line[10:])
