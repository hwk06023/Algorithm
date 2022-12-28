# 시작 지점, 도착 지점이 원 안 좌표일 때 해당 원 카운팅
import math

t = int(input())

for i in range(t):
    cnt = 0
    x_1, y_1, x_2, y_2 = map(int, input().split())
    n = int(input())
    for j in range(n):
        c_x, c_y, r = map(int ,input().split())
        a = math.sqrt((x_1-c_x)**2 + (y_1-c_y)**2)
        b = math.sqrt((x_2-c_x)**2 + (y_2-c_y)**2)
        if(a < r or b < r):
            cnt+=1

        if(a < r and b < r):
            cnt-=1

    print(cnt)