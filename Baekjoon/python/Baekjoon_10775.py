'''import sys

input = sys.stdin.readline

g = int(input())
p = int(input())
li = [int(input()) for _ in range(p)]
gate = [0] * (g + 1)

for i in range(1, p+1):
    gi = li[i-1]
    while gi > 0:
        if gate[gi] == 0:
            gate[gi] = i
            break
        else:
            gi -= 1
    if gi == 0:
        print(i-1)
        break
else:
    print(p)'''

# above code is time limit exceeded
# below code is correct answer
    
import sys

input = sys.stdin.readline

g = int(input())
p = int(input())

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    parent[x] = y

parent = [i for i in range(g+1)]
answer = 0
for _ in range(p):
    gi = int(input())
    x = find(gi)
    if x == 0:
        break
    union(x, x-1)
    answer += 1
print(answer)
