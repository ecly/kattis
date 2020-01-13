import sys

n = int(input())


def verify_line(line):
    whites = line.count("W")
    blacks = line.count("B")
    if whites != blacks:
        return False

    if len(line) < 3:
        return True

    for x, y, z in zip(line, line[1:], line[2:]):
        if x == y and y == z:
            return False

    return True


board = []
for i in range(n):
    board.append(list(input()))


for i in range(n):
    row = "".join(board[i])
    col = "".join(board[j][i] for j in range(n))
    if not verify_line(row) or not verify_line(col):
        print(0)
        sys.exit(0)

print(1)
