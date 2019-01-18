import sys

lines = sys.stdin.readlines()
n = int(lines[0])
words = lines[1].split()

if len(words) != n:
    print("something is fishy")
    sys.exit(0)

counter = 1
for i in range(len(words)):
    if words[i] == "mumble":
        counter += 1
    else:
        val = int(words[i])
        if int(words[i]) != counter:
            print("something is fishy")
            sys.exit(0)

        counter += 1

print("makes sense")
