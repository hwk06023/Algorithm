'''
n = int(input())
li = [[]]

for _ in range(n):
    li.append([])
for i in range(n):
    a, b = map(int, input().split())
    li[a].append(b)

for j in range(n, -1, -1):
    if not li[j]:
        del li[j]
    else:
        li[j] = max(li[j])

print(sum(li))
'''