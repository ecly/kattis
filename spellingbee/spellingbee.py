letters = input()
n = int(input())
matches = 0
for _ in range(n):
    word = input()
    if letters[0] in word and all(c in letters for c in word) and len(word) >= 4:
        print(word)
