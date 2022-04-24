import sys


def get_primes(limit=32000):
    # https://stackoverflow.com/a/568618
    D = {}
    q = 2
    while q < limit:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def get_representations(x, primes):
    r = []
    for p in primes:
        m = x - p
        if m < p:
            break
        if m in primes:
            r.append((p, m))

    return r


def main():
    primes = {p: True for p in get_primes()}
    n = int(sys.stdin.readline())
    for _ in range(n):
        x = int(sys.stdin.readline())
        representations = get_representations(x, primes)
        print(f"{x} has {len(representations)} representation(s)")
        for l, h in representations:
            print(f"{l}+{h}")

        print()


if __name__ == "__main__":
    main()
