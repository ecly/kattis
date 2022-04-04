import sys
from collections import defaultdict

lines = sys.stdin.read().splitlines()
rows = lines[1::2]
grid = [r[2::4] for r in rows]
pieces = defaultdict(list)
for i, r in enumerate(grid):
    row = 8 - i
    for col, piece in zip("abcdefgh", r):
        if piece in ":.":
            continue

        pieces[piece].append((row, col))


def get_locations(types):
    locations = []
    for t in types:
        ps = (
            sorted(pieces[t])
            if types[0].isupper()
            else sorted(pieces[t], key=lambda p: (-p[0], p[1]))
        )
        for r, c in ps:
            loc = "" if t.lower() == "p" else t.upper()
            loc += f"{c}{r}"
            locations.append(loc)

    return locations


white_locations = get_locations("KQRBNP")
print("White:", ",".join(white_locations))
black_locations = get_locations("kqrbnp")
print("Black:", ",".join(black_locations))
