s = input().strip()
print("hiss" if any(x == "s" and y == "s" for x,y in zip(s,s[1:])) else "no hiss")
