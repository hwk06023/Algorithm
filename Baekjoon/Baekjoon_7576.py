''' 
import copy

m, n = map(int, input().split())
li = []
tmp = []
cnt = 0
tmp_cnt = 0

for i in range(n):
    li.append(list(map(int, input().split())))
    li[i].insert(0, -1)
    li[i].append(-1)

li.append([])
li.insert(0, [])
for j in range(m+2):
    li[0].append(-1)
    li[n+1].append(-1)

tmp = copy.deepcopy(li)

while(1):
    for i in range(1, n+1):
        for j in range(1, m+1):
            if li[i][j] == 0:
                if li[i-1][j]==-1 and li[i][j-1]==-1 and li[i][j+1]==-1 and li[i+1][j]==-1:
                    print(-1)
                    exit()
                if li[i-1][j]==1 or li[i][j-1]==1 or li[i][j+1]==1 or li[i+1][j]==1:
                    tmp[i][j] = 1
            else:
                tmp_cnt += 1
    if tmp_cnt == m*n:
        break
    li = copy.deepcopy(tmp)
    cnt += 1
    tmp_cnt=0

print(cnt)
'''
# 위에 시간초과.. 해설봣슴니다..

from collections import deque

m, n = map(int, input().split())
li = []
queue = deque([])
cnt = 0

for i in range(n):
    li.append(list(map(int, input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            queue.append([i, j])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and li[nx][ny] == 0:
            li[nx][ny] = li[x][y] + 1
            queue.append([nx, ny])

for i in li:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))
print(cnt - 1)
