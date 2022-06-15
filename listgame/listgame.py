import math

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def get_primes(limit=10**9):
    # https://stackoverflow.com/a/568618
    d = {}
    q = 2
    while q < limit:
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]

        q += 1


def main():
    x = int(input())

    rem = x
    k = 1
    while not is_prime(rem):
        for d in get_primes():
            if rem % d == 0 or d >= rem:
                break

        if d >= rem:
            break

        rem /= d
        k += 1

    print(k)


if __name__ == "__main__":
    main()
