import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
n_li = list(map(int, input().split()))  

flag = permutations(n_li, m)

li = []
for i in flag:
    li.append(i)

li.sort()
for x in li:
    print(' '.join(map(str, x)), end='\n')

