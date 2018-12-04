s = input().strip()
out = ""
i = 0
while i < len(s):
    c = s[i]
    out += c
    if i > len(s) - 3:
        break
    if c in "aeiou" and c == s[i+2] and s[i+1] == "p":
        i += 3
    else:
        i += 1

print(out)
