import sys

input = sys.stdin.readline

n = list(input())
result = 0

s = 1
for i in range(0, 18):
    if i % 2 == 0:
        s += int(n[i]) * (10 - (i // 2))
    else:
        s += int(n[i]) * (10 - (i // 2))
s %= 19

