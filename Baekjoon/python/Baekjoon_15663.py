import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
n_li = list(map(int, input().split()))  
n_li.sort()

flag = permutations(n_li, m)

li = list(set(flag))
li.sort()

for x in li:
    print(' '.join(map(str, x)), end='\n')
    