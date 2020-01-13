import fileinput
fbi_blimps = []
for idx, line in enumerate(fileinput.input(), 1):
    if "FBI" in line:
        fbi_blimps.append(idx)

if fbi_blimps:
    print(*fbi_blimps)
else:
    print("HE GOT AWAY!")
