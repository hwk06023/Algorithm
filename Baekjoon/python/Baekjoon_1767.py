import sys

input = sys.stdin.readline

k = int(input())

for _ in range(k):
    v, e = map(int , input().split())
    node = [[] for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)

