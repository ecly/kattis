import re
s = input()
p = input()
if p == s or p.swapcase() == s or re.match(f"\d{p}", s) or re.match(f"{p}\d", s):
    print("Yes")
else:
    print("No")
