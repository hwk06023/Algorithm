import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[1])

queue = []
max_idx = 0
for i in range(n):
    if queue:
        if queue[0] <= arr[i][1]:
            queue.pop(0)
        queue.append(arr[i][2])
        queue.sort()
    else:
        queue.append(arr[i][2])
    max_idx = max(max_idx, len(queue))

print(max_idx)