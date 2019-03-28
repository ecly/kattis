res = []
for c in input():
    if c == "<":
        res.pop()
    else:
        res.append(c)

print(''.join(res))
