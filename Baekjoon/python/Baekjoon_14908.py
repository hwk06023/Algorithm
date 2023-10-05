import sys

input = sys.stdin.readline

n = int(input())

li = []
for i in range(1,n+1):
    t, s = map(int, input().split())
    li.append([t/s, i])

li.sort(key=lambda x: x[0])

flag_li = []
for x in li:
    flag_li.append(x[1])

print(' '.join(map(str, flag_li)))