r, c, zr, zc = [int(x) for x in input().split()]
m = []
for _ in range(r * zr):
    m.append(["*"] * c * zc)

for row in range(r):
    for col, char in enumerate(input()):
        r_offset = row*zr
        c_offset = col*zc
        for rv in range(r_offset, r_offset+zr):
            for rc in range(c_offset, c_offset+zc):
                m[rv][rc]=char

for row in m:
    print(''.join(row))
