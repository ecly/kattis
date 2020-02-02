from string import ascii_uppercase

cipher = input()
secret = input()

for i, c in enumerate(cipher):
    shift = ascii_uppercase.index(secret[i])
    cipher_i = ascii_uppercase.index(c)
    secret += ascii_uppercase[cipher_i - shift]

print(secret[-len(cipher) :])
