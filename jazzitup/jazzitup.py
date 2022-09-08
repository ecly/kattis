import itertools

squares = list(
    itertools.takewhile(lambda x: x < 10**5, (i**2 for i in itertools.count(2)))
)


def is_squarefree(i):
    return not any(i % s == 0 for s in squares)


def main():
    n = int(input())
    for m in range(2, n):
        notes = n * m
        if is_squarefree(notes):
            return m

    return None


if __name__ == "__main__":
    print(main())
