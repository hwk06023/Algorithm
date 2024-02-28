import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

sum_value = 0
i_end = 0

cnt = 0
for i_start in range(n):
    while sum_value < m and i_end < n:
        sum_value += li[i_end]
        i_end += 1
    if sum_value == m:
        cnt += 1
    sum_value -= li[i_start]

print(cnt)