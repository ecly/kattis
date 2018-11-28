import sys
sets = []
for l in map(lambda x: x.strip(), sys.stdin.readlines()[:-1]):
    if l.isdigit():
        sets.append([])
        continue

    sets[-1].append(l)

for idx, s in enumerate(sets, 1):
    print("SET", idx)
    pyramid = (s[::2] + s[1::2][::-1])
    for n in pyramid:
        print(n)
