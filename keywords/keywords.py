# golf solution
# print(len({input().strip().lower().replace("-","")for _ in range(int(input()))}))
import sys
n = int(sys.stdin.readline())
keywords = set()
for _ in range(n):
    keyword = sys.stdin.readline().strip()
    keyword = keyword.lower().replace("-", " ")
    keywords.add(keyword)

print(len(keywords))
