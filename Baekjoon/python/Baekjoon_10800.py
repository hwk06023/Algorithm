import sys

input = sys.stdin.readline

n = int(input())
balls = []
result = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    balls.append([a, b, i])

balls.sort(key=lambda x: x[1])
color = [0] * (n + 1)
total = 0
idx = 0
for i in range(n):
    while balls[idx][1] < balls[i][1]:
        total += balls[idx][1]
        color[balls[idx][0]] += balls[idx][1]
        idx += 1
    result[balls[i][2]] = total - color[balls[i][0]]

for x in result:
    print(x)
