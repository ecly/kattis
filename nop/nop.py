padding = 0
for i, c in enumerate(input()):
    if c.islower():
        continue

    rem = (i + padding) % 4
    if rem:
        padding += (4 - rem)

print(padding)
