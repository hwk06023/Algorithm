'''
from sys import stdin

n = int(stdin.readline())

li = [[], []]
cnt = 0

for i in range(n):
    a, b = map(int, stdin.readline().split())
    li[0].append(a)
    li[1].append(b)

while(1):
    last_min = li[1][0]
    tmp = 0

    for i in range(1, len(li[1])):
        if last_min > li[1][i]:
            last_min = li[1][i]
            tmp = i
    del li[0][tmp]
    del li[1][tmp]
    
    for i in range(len(li[0])-1, -1, -1):
        if li[0][i] < last_min:
            del li[0][i]
            del li[1][i]
    cnt += 1
   
    if len(li[0]) == 0:
        break

print(cnt)
'''
#위에 시간초과

from sys import stdin

n = int(stdin.readline())

li = []

for i in range(n):
    li.append(list(map(int, stdin.readline().split())))

li = sorted(li, key=lambda k: k[0])
li = sorted(li, key=lambda k: k[1])

last = 0
cnt = 0

for i, j in li:
    if i >= last:
        last = j
        cnt += 1
        
print(cnt)