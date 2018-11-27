import sys

position = 1
for c in sys.stdin.read().upper():
    if c == "A":
        if position == 1:
            position = 2
        elif position == 2:
            position = 1
    if c == "B":
        if position == 2:
            position = 3
        elif position == 3:
            position = 2
    if c == "C":
        if position == 3:
            position = 1
        elif position == 1:
            position = 3

print(position)
