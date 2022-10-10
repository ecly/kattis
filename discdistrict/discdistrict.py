# A clever solution
print(input(), 1)

# A brute force solution
# import math
#
# r = int(input())
# best = 1 << 31
# best_i, best_j = None, None
# for i in range(r, 0, -1):
#     for j in range(r - i + 1, 0, -1):
#         ed = math.sqrt(i**2 + j**2)
#         if ed < r:
#             break
#
#         if ed < best:
#             best = ed
#             best_i, best_j = i, j
#
# print(best_i, best_j)
