import fileinput
for line in fileinput.input():
    print("yes" if "problem" in line.lower() else "no")
