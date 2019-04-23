import fileinput
words = set()
for line in fileinput.input():
    words.update(line.split())

compounds = set()
words = list(words)
for idx, w in enumerate(words):
    for w1 in words[idx+ 1:]:
        compounds.add(w + w1)
        compounds.add(w1 + w)

print("\n".join(sorted(list(compounds))))
