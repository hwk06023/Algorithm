import sys
input = sys.stdin.readline

INF = float('inf')

n, m = map(int, input().split())
start = int(input())
edges = [()]
distance = [INF] * (n+1)

for _ in range(n):
    a, b, c = map(int, input().split())
    # edges[0]은 시작(현재) 노드, edges[1]은 도착(향해진) 노드, edges[2]은 거리(소모)값
    edges.append((a, b, c))

def bellmanford(start):
    distance[start] = 0

    for i in range(n):
        for j in range(m):
            now_node = edges[j][0]
            targeted_node = edges[j][1]
            cost = edges[j][2]

            if (distance[now_node] != INF) and (distance[targeted_node] > distance[now_node] + cost):
                distance[targeted_node] = distance[now_node] + cost

            if i == n-1:
                return True
    return False

cant = bellmanford(start)

if cant:
    print("한무리필")
else:
    # INF = 안 닿음. 도달 불가.
    print(distance)
    