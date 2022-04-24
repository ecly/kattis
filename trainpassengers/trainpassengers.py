def is_possible(capacity, stops):
    c = 0
    for left, entered, stayed in stops:
        if left > c:
            return False
        c += entered - left
        if c > capacity or stayed and c < capacity:
            return False

    return not bool(c)


def main():
    capacity, stops = map(int, input().split())
    stops = [tuple(map(int, input().split())) for _ in range(stops)]
    print("possible" if is_possible(capacity, stops) else "impossible")


if __name__ == "__main__":
    main()
