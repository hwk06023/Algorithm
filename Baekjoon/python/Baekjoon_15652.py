import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())

flag = combinations_with_replacement(range(1, n+1), m)

li = []
for i in flag:
    li.append(i)

li.sort()
for x in li:
    print(' '.join(map(str, x)), end='\n')

