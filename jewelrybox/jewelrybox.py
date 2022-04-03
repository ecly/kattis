def volume(x, y, h):
    return (x - h * 2) * (y - h * 2) * h


def main():
    t = int(input())
    eps = 1e-6
    for _ in range(t):
        x, y = map(int, input().split())
        l = eps
        h = max(x, y) / 2
        while abs(h - l) > eps:
            m1 = l + (h - l) * 1 / 3
            m2 = l + (h - l) * 2 / 3
            if volume(x, y, m1) < volume(x, y, m2):
                l = m1
            else:
                h = m2

        print(f"{volume(x, y, l):.6f}")


if __name__ == "__main__":
    main()
