import sys

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
i2c = {i: c for i, c in enumerate(alphabet)}
c2i = {c: i for i, c in i2c.items()}
for line in sys.stdin.readlines()[:-1]:
    N, s = line.split()
    rotation = int(N)
    print("".join(
          map(lambda i: i2c[i],
          map(lambda i: (i + rotation) % len(alphabet),
          map(lambda c: c2i[c], s[::-1]))))
         )
