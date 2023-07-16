import re
_n = input()
print(max(map(int, re.findall(r"\d+", input()))))
