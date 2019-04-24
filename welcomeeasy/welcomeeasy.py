# since more_itertools not available
def locate(elem, enum):
    return [i for i in range(len(enum)) if enum[i] == elem]

def rec(t, i):
    if not i: return 1
    if not t: return 0
    return sum(rec(t[o + 1:], i[1:]) for o in locate(i[0], t))

T = int(input())
for case in range(1, T + 1):
    test = input()
    res = rec(test, "welcome to code jam")
    print("Case #%d: %s" % (case, str(res + 10000)[-4:]))
