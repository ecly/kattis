def main(l, n):
    # l = loo roll's length
    # n = used per visit
    for k in range(1, n + 1):
        needed_paper = n
        for _ in range(k):
            rem = l % needed_paper
            if rem == 0:
                return k

            needed_paper -= rem


if __name__ == "__main__":
    l, n = map(int, input().split())
    print(main(l, n))
