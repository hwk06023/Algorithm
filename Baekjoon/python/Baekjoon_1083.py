import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(n):
    max_idx = i
    for j in range(i+1, min(i+s+1, n)):
        if arr[max_idx] < arr[j]:
            max_idx = j
    s -= (max_idx - i)
    arr.insert(i, arr.pop(max_idx))
    if s == 0:
        break
print(*arr)