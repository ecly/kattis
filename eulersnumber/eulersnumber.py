def main():
    n = int(input())
    fac = 1  # 0! = 1
    total = 1
    for i in range(1, n + 1):
        fac *= i
        total += 1 / fac

    print(total)


if __name__ == "__main__":
    main()
