T = int(input())

# num is alwasy in base10
def enc(num, lang):
    if num == 0:
        return ""
    rem = num // len(lang)
    return enc(rem, lang) + lang[num % len(lang)]

def dec(num, lang):
    res = 0
    base = len(lang)
    for idx, n in enumerate(num[::-1]):
        x = lang.index(n)
        res += (base ** idx) * x

    return res

for t in range (1, T + 1):
    num, src, tgt = input().split()
    decimal = dec(num, src)
    print("Case #%d: %s" % (t, enc(decimal, tgt)))
