import textwrap, collections
s = input()
words = textwrap.wrap(s, len(s) // 3)
print(collections.Counter(words).most_common(1)[0][0])
