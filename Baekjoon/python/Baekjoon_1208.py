import sys

input = sys.stdin.readline

n, s = map(int, input().split())
li = list(map(int, input().split()))

left_dict = {}
right_dict = {}

def dfs(idx, end, sum, dict):
    if idx == end:
        if sum in dict:
            dict[sum] += 1
        else:
            dict[sum] = 1
        return
    dfs(idx + 1, end, sum, dict)
    dfs(idx + 1, end, sum + li[idx], dict)

dfs(0, n // 2, 0, left_dict)
dfs(n // 2, n, 0, right_dict)

flag = 0
for key in left_dict:
    if s - key in right_dict:
        flag += left_dict[key] * right_dict[s - key]

if s == 0:
    flag -= 1

print(flag)