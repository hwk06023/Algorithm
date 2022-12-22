'''
n = int(input())
a = 1
k = 0
    
for i in range(1, n+1):
    a*=i

a = str(a)

for x in a:
    if x=='0':
        k += 1
print(k)
'''

# 위에는 좀 비교적 무식하게 0 세는 방법

n = int(input())
i_2 = 0
i_5 = 0
tmp = 0

for x in range(1, n+1):
    tmp = x
    if x % 2 ==0: 
        while(tmp%2 == 0):
            tmp /= 2
            i_2 += 1
    tmp = x
    if x % 5 ==0:
        while(tmp%5 == 0):
            tmp /= 5
            i_5 += 1

print(min(i_2, i_5))