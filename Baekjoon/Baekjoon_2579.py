num = int(input())

li = []
total = [0] * num

for i in range(num):
    li.append(int(input()))

# print(li)

total[0] = li[0]
total[1] = li[0] + li[1]
total[2] = max(li[0]+li[2], li[1]+li[2])
total[3] = max(total[1] + li[2], total[0] + li[2]+ li[3])
'''
total[4] = max(total[2] + li[4], total[1] + li[3]+ li[4])
# 규칙적
'''
for i in range(3, num):
    total[i] = max(total[i-2] + li[i], total[i-3] + li[i-1] + li[i])

# print(total)
print(total[num-1])