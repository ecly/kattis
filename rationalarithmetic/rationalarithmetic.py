from fractions import Fraction


def main():
    n = int(input())
    for _ in range(n):
        x1, y1, op, x2, y2 = input().split()
        left = Fraction(int(x1), int(y1))
        right = Fraction(int(x2), int(y2))
        if op == "+":
            res = left + right
        elif op == "-":
            res = left - right
        elif op == "*":
            res = left * right
        elif op == "/":
            res = left / right

        print(f"{res.numerator} / {res.denominator}")


if __name__ == "__main__":
    main()
