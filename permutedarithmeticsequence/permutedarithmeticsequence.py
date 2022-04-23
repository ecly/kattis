def is_arithmetic(s):
    d = s[1] - s[0]
    return all(y - x == d for x, y in zip(s, s[1:]))


def check_sequence(s):
    if is_arithmetic(s):
        return "arithmetic"

    if is_arithmetic(sorted(s)):
        return "permuted arithmetic"

    return "non-arithmetic"


def main():
    n = int(input())
    for _ in range(n):
        seq = list(map(int, input().split()))[1:]
        print(check_sequence(seq))


if __name__ == "__main__":
    main()
