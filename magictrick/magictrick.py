s = input().strip()
print("0" if len(s) != len(set(s)) else "1")
