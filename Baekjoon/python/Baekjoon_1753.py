import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = float('inf')
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [INF] * (V + 1)

def dijkstra(start):
    distance[start] = 0
    queue = [(0, start)]

    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist:
            continue

        for v, w in graph[node]:
            cost = dist + w

            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
