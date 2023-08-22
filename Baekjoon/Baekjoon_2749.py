n = int(input())

li = [0, 1]
for i in range(n-1):
    li.append(li[0]+li[1])
    del li[0]

print(li[1] % 1000000)