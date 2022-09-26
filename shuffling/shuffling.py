import math


def shuffle(deck, is_out):
    mid = len(deck) / 2
    mid = math.ceil(mid) if is_out else math.floor(mid)
    first_half = deck[:mid]
    second_half = deck[mid:]
    if not is_out:
        first_half, second_half = second_half, first_half

    deck[::2] = first_half
    deck[1::2] = second_half


def main():
    n, in_or_out = input().split()
    n = int(n)
    start_deck = list(range(n))

    is_out = in_or_out == "out"
    deck = start_deck[::]
    shuffle(deck, is_out)
    shuffles = 1
    while deck != start_deck:
        shuffle(deck, is_out)
        shuffles += 1

    return shuffles


if __name__ == "__main__":
    print(main())
