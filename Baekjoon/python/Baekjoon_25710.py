import sys
from itertools import combinations_with_replacement
from collections import Counter

input = sys.stdin.readline

n = int(input())
cnt_li = Counter(map(int, input().split()))

comb_li = list(combinations_with_replacement(cnt_li, 2))

flag = 1
for x in comb_li:
    if (x[0] != x[1]) or cnt_li[x[0]] > 1:
        tmp_value = x[0]*x[1]
        tmp_flag = 0
        while tmp_value:
                tmp_flag += tmp_value % 10
                tmp_value //= 10
        flag = max(flag, tmp_flag)
print(flag)