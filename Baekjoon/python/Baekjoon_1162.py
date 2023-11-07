import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [[float('inf') for _ in range(k+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start, 0))
    distance[start][0] = 0

    while q:
        dist, now, cnt = heapq.heappop(q)

        if distance[now][cnt] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]][cnt]:
                distance[i[0]][cnt] = cost
                heapq.heappush(q, (cost, i[0], cnt))

            if cnt < k and dist < distance[i[0]][cnt+1]:
                distance[i[0]][cnt+1] = dist
                heapq.heappush(q, (dist, i[0], cnt+1))

dijkstra(1)
print(min(distance[n]))