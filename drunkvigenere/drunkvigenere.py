from string import ascii_uppercase
i2c = dict(enumerate(ascii_uppercase))
c2i = {c: i for i, c in i2c.items()}

c, k = input(), input()
decrypted = ""
for i, (cipher, key) in enumerate(zip(c, k)):
    ci, ck = c2i[cipher], c2i[key]
    if i % 2 == 0:
        d = ci - ck
        if d < 0:
            d += 26
        decrypted += i2c[d]
    else:
        decrypted += i2c[(ci + ck) % 26]

print(decrypted)
