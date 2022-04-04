BOARD_TEMPLATE = """
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
"""

R_TO_IDX = {8 - i: i * 2 + 1 for i in range(8)}
C_TO_IDX = {c: 2 + i * 4 for c, i in zip("abcdefgh", range(8))}


def loc_to_idx(loc):
    col = loc[-2]
    row = loc[-1]
    return C_TO_IDX[col], R_TO_IDX[int(row)]


def parse(input_):
    return [p for p in input_.split(": ")[1].split(",") if p]


def main():
    board = BOARD_TEMPLATE.strip().split("\n")
    board = [list(r) for r in board]
    white = parse(input())
    black = parse(input())
    for p in white:
        c, r = loc_to_idx(p)
        board[r][c] = p[0] if len(p) == 3 else "P"

    for p in black:
        c, r = loc_to_idx(p)
        board[r][c] = p[0].lower() if len(p) == 3 else "p"

    print("\n".join("".join(r) for r in board))


if __name__ == "__main__":
    main()
