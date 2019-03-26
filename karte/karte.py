cards = []
test = input()
for i in range(0, len(test), 3):
    cards.append(test[i:i+3])

if len(cards) != len(set(cards)):
    print("GRESKA")
else:
    p = 13 - test.count("P")
    k = 13 - test.count("K")
    h = 13 - test.count("H")
    t = 13 - test.count("T")
    print(p, k, h, t)
