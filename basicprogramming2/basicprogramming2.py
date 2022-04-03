from collections import Counter
from itertools import dropwhile, takewhile


def action1(a):
    ns = list(takewhile(lambda x: x < 7777, sorted(a)))
    for i, x in enumerate(ns):
        for y in ns[i + 1 :]:
            s = x + y
            if s == 7777:
                return "Yes"

            if s > 7777:
                break

    return "No"


def action2(a):
    return "Unique" if len(a) == len(set(a)) else "Contains duplicate"


def action3(a):
    i, c = Counter(a).most_common(1)[0]
    return i if c > len(a) / 2 else -1


def action4(a):
    a = sorted(a)
    if len(a) % 2 == 1:
        return str(a[len(a) // 2])

    m = len(a) // 2
    return f"{a[m-1]} {a[m]}"


def action5(a):
    a = sorted(a)
    ns = takewhile(lambda i: i < 1000, dropwhile(lambda i: i < 100, a))
    return " ".join(str(i) for i in ns)


def main():
    _n, t = map(int, input().split())
    a = list(map(int, input().split()))

    action = {1: action1, 2: action2, 3: action3, 4: action4, 5: action5}[t]
    print(action(a))


if __name__ == "__main__":
    main()
