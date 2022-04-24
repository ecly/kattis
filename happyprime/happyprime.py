import math


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def is_happy(prime):
    digits = [int(c) for c in str(prime)]
    seen = set()
    while True:
        squared_digit_sum = 0
        for d in digits:
            squared_digit_sum += d**2

        if squared_digit_sum in seen:
            break

        seen.add(squared_digit_sum)

        if squared_digit_sum <= 1:
            return bool(squared_digit_sum)

        digits = [int(c) for c in str(squared_digit_sum)]


def main():
    p = int(input())
    for _ in range(p):
        k, m = map(int, input().split())
        print(k, m, "YES" if is_prime(m) and is_happy(m) else "NO")


if __name__ == "__main__":
    main()
