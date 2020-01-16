def main():
    input_ = input().split()
    height = int(input_[0]) + 1
    path = "" if len(input_) == 1 else input_[1]
    root = 2 ** height - 1
    depth = len(path)
    if depth == 0:
        print(root)
    else:
        min_ = root - 2 ** (depth + 1) + 2
        offset = sum(2 ** (depth - i - 1) for i, p in enumerate(path) if p == "L")
        print(min_ + offset)


if __name__ == "__main__":
    main()
