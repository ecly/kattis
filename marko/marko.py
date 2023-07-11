n = int(input())
words = [input().strip() for _ in range(n)]
keyboard = {
    1: "",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
}
s = input()
for idx, number in enumerate(map(int, s)):
    words = [w for w in words if w[idx] in keyboard[number]]

print(len(words))
