import fileinput
defs = {}
for line in fileinput.input():
    if line.startswith("def"):
        var, val = line.strip().split()[1:]
        defs[var] = val
    elif line.startswith("calc"):
        tokens = line.strip().split()[1:-1]
        if any(x not in defs for x in tokens[::2]):
            print(line[5:].strip() + " unknown")
        else:
            eq = list(map(lambda t: defs.get(t, t), tokens))
            res = eval(" ".join(eq))
            invs = {v: k for k, v in defs.items()}
            print(line[5:].strip() + " " + invs.get(str(res), "unknown"))
    else:
        defs.clear()
