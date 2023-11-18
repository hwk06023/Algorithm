import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
visited =[['',0] for _ in range(20001)]
visited_num = 0

for _ in range(t):
    n = int(input())
    q = deque([1])
    visited[1] = ['1', visited_num]
    visited_num += 1

    while q:
        now = q.popleft()
        if now == 0:
            break
        for i in range(2):
            next = (now*10 + i) % n
            if visited[next][1] != visited_num:
                visited[next] = [visited[now][0] + str(i), visited_num]
                q.append(next)
    print(visited[0][0])


