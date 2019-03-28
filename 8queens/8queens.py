import fileinput
def is_valid(grid):
    # each row/column should have one queen
    if any(row.count("*") != 1 for row in grid):
        return False
    if any(col.count("*") != 1 for col in [*zip(*grid)]):
        return False

    # check diagonals
    starts = [(x, 0) for x in range(8)] + [(0, y) for y in range(8)]
    for s in starts:
        cxe, cye = s
        cxw, cyw = cxe, 7 - cye
        count_e = 0
        count_w = 0
        while cxe < 8 and cye < 8:
            count_e += grid[cye][cxe] == "*"
            count_w += grid[cyw][cxw] == "*"
            cxe, cye = cxe + 1, cye + 1
            cxw, cyw = cxw + 1, cyw - 1

        if count_e > 1 or count_w > 1:
            return False

    return True



input_ = []
for line in fileinput.input():
    input_.append(list(line.strip()))

print("valid" if is_valid(input_) else "invalid")
