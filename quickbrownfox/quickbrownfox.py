for _ in range(int(input())):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    test = input().lower()
    present = set(filter(lambda c: c.isalpha(), test))
    if len(alphabet) == len(present):
        print("pangram")
    else:
        print("missing", ''.join(sorted(alphabet - present)))
