n = int(input())
s = list(input())
s_ = s[::]
for i in range(n):
    if s[i] == "1":
        for j in range(i, min(n, i + 3)):
            s_[j] = "1"

print(s_.count("1"))
