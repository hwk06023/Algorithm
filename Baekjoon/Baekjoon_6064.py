'''
n = int(input())

for i in range(n):
    li = list(map(int, input().split()))

    x_cnt = 1
    y_cnt = 1
    cnt = 1
    while(1):
        if cnt > 1 and x_cnt == 1 and y_cnt == 1:
            print(-1)
            break
        if x_cnt == li[2] and y_cnt == li[3]:
            print(cnt)
            break
        if x_cnt < li[0]:
            x_cnt += 1
        elif x_cnt == li[0]:
            x_cnt = 1

        if y_cnt < li[1]:
            y_cnt += 1
        elif y_cnt == li[1]:
            y_cnt = 1
        cnt += 1
'''
# 위에 시간초과

n = int(input())

def gcd(a, b): 
    for i in range(min(a, b), 1, -1):
        if a%i==0 and b%i==0:
            return i

def lcm(a, b):
    return a * b / gcd(a, b)

for i in range(n):
    li = list(map(int, input().split()))

    cnt = li[2].
    while(1):
        if cnt > lcm(li[0], li[1]):
            print('-1')
            break
        cnt += li[0]
        y = cnt % li[1]

        if y == li[3]:
            print(cnt)
            break
