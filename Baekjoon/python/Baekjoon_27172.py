import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
num_li = [False] * 1000001
flag_li = [0] * 1000001

for x in li:
    num_li[x] = True

for i in range(n):
    li_i = li[i]
    tmp = li_i * 2
    while tmp < 1000001:
        if num_li[tmp]:
            flag_li[li_i] += 1
            flag_li[tmp] -= 1
        tmp += li_i

for i in range(n):
    print(flag_li[li[i]], end=' ')
print()
