import fileinput, itertools
numbers = list(map(int, fileinput.input()))
for perm in itertools.permutations(numbers, 7):
    if sum(perm) == 100:
        print('\n'.join(list(map(str, perm))))
        break
