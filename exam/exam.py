k = int(input())
mine = input()
friends = input()
qs = len(mine)
same_count = sum(a==b for a, b in zip(mine, friends))
diff_count = qs - same_count
print(min(k, same_count) + min(qs - k, diff_count))
