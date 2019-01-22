import sys
for line in sys.stdin.readlines()[:-1]:
    sweet, sour = map(int, line.split())
    if sweet + sour == 13:
        print("Never speak again.")
    elif sour > sweet:
        print("Left beehind.")
    elif sour == sweet:
        print("Undecided.")
    else:
        print("To the convention.")
