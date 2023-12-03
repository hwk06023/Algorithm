import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())
n_li = list(map(int, input().split()))  
n_li.sort()

flag = combinations_with_replacement(n_li, m)

li = list(set(flag))
li.sort()

for x in li:
    print(' '.join(map(str, x)), end='\n')
    