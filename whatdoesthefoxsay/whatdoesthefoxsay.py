import sys
T = int(input())
cases = map(lambda s: s.split('\n'), sys.stdin.read().split("\nwhat does the fox say?\n"))
for case in cases:
    fox = case[0].split()
    not_fox = set()
    for sound in case[1:]:
        not_fox.add(sound.split()[-1])

    print(" ".join(filter(lambda s: s not in not_fox, fox)))
