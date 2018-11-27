last = ""
out = ""
for x in input().strip():
    if last != x:
        out += x

    last = x

print(out)
