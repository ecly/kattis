import fileinput
seen = set()
for line in fileinput.input():
    words = line.strip().split()
    res = []
    for w in words:
        if w.lower() in seen:
            res.append(".")
        else:
            res.append(w)
            seen.add(w.lower())

    print(" ".join(res))
