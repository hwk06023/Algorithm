import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

tmp_li = [-10000000001]

for i in range(n):
    if li[i] > tmp_li[-1]:
        tmp_li.append(li[i])
    else:
        tmp = bisect_left(tmp_li, li[i])
        tmp_li[tmp] = li[i]

print(len(tmp_li)-1)