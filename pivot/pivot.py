def main():
    n = int(input())
    ints = list(map(int, input().split()))

    fwd = set()
    bwd = set()

    maximum = 0
    for idx, x in enumerate(ints):
        if x > maximum:
            fwd.add(idx)
            maximum = x

    minimum = 1 << 30
    for idx, x in enumerate(ints[::-1], 1):
        if x < minimum:
            bwd.add(n - idx)
            minimum = x

    print(len(fwd.intersection(bwd)))

if __name__ == "__main__":
    main()
