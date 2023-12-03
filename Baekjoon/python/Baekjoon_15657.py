import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())
n_li = list(map(int, input().split()))  
n_li = sorted(n_li)

flag = combinations_with_replacement(n_li, m)

li = []
for x in flag:
    li.append(list(x))

for x in li:
    print(' '.join(map(str, x)), end='\n')