from sys import stdin, stdout


def main():
    n = int(stdin.readline())
    strings = [stdin.readline().rstrip() for _ in range(n)]
    root = list(range(n))
    next_ = list(range(n))
    a = 0
    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, stdin.readline().split())
        r = a

        # elements to update root
        to_update = []
        while root[r] != r:
            to_update.append(r)
            r = root[root[r]]

        for i in to_update:
            root[i] = b

        root[r] = b
        next_[r] = b

    i = a
    for _ in range(n - 1):
        stdout.write(strings[i])
        i = next_[i]

    stdout.write(strings[i])


if __name__ == "__main__":
    main()
