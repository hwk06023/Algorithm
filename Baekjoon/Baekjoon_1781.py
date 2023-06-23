'''
n = int(input())
li = [[]]

for _ in range(n):
    li.append([])
for i in range(n):
    a, b = map(int, input().split())
    li[a].append(b)

for j in range(n, -1, -1):
    if not li[j]:
        del li[j]
    else:
        li[j] = max(li[j])

print(sum(li))
'''
import heapq
import sys

input = sys.stdin.readline

n = int(input())

li = []
r_li = []

for i in range(n):
    time, item = map(int, input().split())
    heapq.heappush(li, (time, -item))

while li:
    time, item = heapq.heappop(li)
    item = -item
    if len(r_li) < time:
        heapq.heappush(r_li, item)
    else:
        if r_li and item > r_li[0]:
            heapq.heappop(r_li)
            heapq.heappush(r_li, item)

print(sum(r_li))