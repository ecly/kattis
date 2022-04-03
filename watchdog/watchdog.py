def dist(x1, y1, x2, y2):
    return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5


def find_shortest(s, h):
    hatches = {tuple(map(int, input().split())) for _ in range(h)}
    for x in range(s):
        for y in range(s):
            if (x, y) in hatches:
                continue

            max_leash_length = min(x, s - x, y, s - y)
            leash_length = max(dist(x, y, hx, hy) for hx, hy in hatches)
            if leash_length <= max_leash_length:
                return x, y

    return None


def main():
    n = int(input())
    for _ in range(n):
        s, h = map(int, input().split())
        res = find_shortest(s, h)
        if res:
            print(*res)
        else:
            print("poodle")


if __name__ == "__main__":
    main()
