n, m = map(int, input().split())
plain = list(map(ord, input()))
cipher = list(map(ord, input()))
plain = [ord(" ") for _ in range(m - n)] + plain
for i in range(m - 1, n - 1, -1):
    plain[i - n] = ord("a") + (26 + cipher[i] - plain[i]) % 26

print("".join(map(chr, plain)))
