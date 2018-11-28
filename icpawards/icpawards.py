import sys
board = []
seen = set()
for team in sys.stdin.readlines()[1:]:
    uni, name = team.split()
    if uni in seen:
        continue

    seen.add(uni)
    board.append(team)

    if len(board) >= 12:
        break

print('\n'.join(board))
