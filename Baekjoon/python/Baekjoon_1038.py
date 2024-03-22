import sys
from itertools import combinations

input = sys.stdin.readline

li = []
n = int(input())

for i in range(1, 11):
    for x in combinations('1234567890', i):
        tmp = int("".join(map(str, sorted(x, reverse=True))))
        li.append(tmp)

li.sort()

if n < len(li):
    print(li[n])
else:
    print(-1) 

