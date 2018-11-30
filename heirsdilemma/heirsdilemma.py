l, h = [int(x) for x in input().split()]
possible = 0
for i in range(l, h):
    i_str = str(i)
    if len(set(i_str)) != len(i_str) or "0" in i_str:
        continue

    nums = [int(c) for c in i_str]
    if all(i % n == 0 for n in nums):
        possible += 1

print(possible)
