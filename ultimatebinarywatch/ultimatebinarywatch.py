bs = [format(int(c), '04b') for c in input()]
for i in range(4):
    b = ["*" if b[i] == "1" else "." for b in bs]
    print(f"{b[0]} {b[1]}   {b[2]} {b[3]}")
