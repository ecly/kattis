fst = input()
snd = input()

# padding
max_len = max(len(fst), len(snd))
if len(fst) == max_len:
    snd = "0" * (max_len - len(snd)) + snd

elif len(snd) == max_len:
    fst = "0" * (max_len - len(fst)) + fst

def solve(x, y):
    res = [c1 for c1, c2 in zip(x, y) if c1 >= c2]
    return int("".join(res)) if res else "YODA"


print(solve(fst, snd))
print(solve(snd, fst))
