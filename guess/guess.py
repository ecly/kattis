import sys
l, h = 1, 1000
for i in range(10):
    guess = l + (h-l)//2
    print(guess)
    sys.stdout.flush()
    response = input()
    if response == "correct":
        break

    if response == "lower":
        h = guess - 1
    else:
        l = guess + 1
