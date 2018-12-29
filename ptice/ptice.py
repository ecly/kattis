N = int(input())
adrian = "ABCABCABCABC"
bruno = "BABCBABCBABC"
goran = "CCAABBCCAABB"

a = 0
b = 0
g = 0
for idx, c in enumerate(input()):
    a += adrian[idx % len(adrian)] == c
    b += bruno[idx % len(bruno)] == c
    g += goran[idx % len(goran)] == c

best = max(a, b, g)
print(best)
if a == best:
    print("Adrian")
if b == best:
    print("Bruno")
if g == best:
    print("Goran")
