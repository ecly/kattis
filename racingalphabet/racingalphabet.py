import math
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
circle = {c: i for i, c in enumerate(alphabet)}
circumference = 60 * math.pi
letter_dist = circumference / len(circle)
N = int(input())
for _ in range(N):
    aphorism = input()
    total = 0
    pos = circle[aphorism[0]]
    for c in aphorism:
        new_pos = circle[c]
        space = abs(pos - new_pos)

        # go other way around
        if space > len(alphabet) / 2:
            l, h = sorted([pos, new_pos])
            space = l + 28 - h

        pos = new_pos
        dist = space * letter_dist
        time = dist / 15 + 1
        total += time

    print(total)
