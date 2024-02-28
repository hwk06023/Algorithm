import sys
import heapq
input = sys.stdin.readline

INF = float('inf')

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(n):
    a, b, c = map(int, input().split())
    # graph[0]은 향해진 노드, graph[1]은 거리(소모)값
    graph[a].append((b, c))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (start, 0))
    distance[start] = 0

    while queue:
        node, dist = heapq.heappop(queue)
        if dist > distance[node]:
            continue

        for x in graph[node]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(queue, (cost, x[0]))

dijkstra(start)
# dinstance[노드]에 start ~ 노드 거리들 담아짐. 거리가 여전히 INF면 안 이어진(도달불가) 친구임.
