import sys, math
n = int(input())

li = []
m_a = 0
m_b = 0
for i in range(n):
    li.append(list(map(int, input().split())))
    m_a += li[i][0]
    m_b += li[i][1]

x_point = round(m_a/n, 6)
y_point = round(m_b/n, 6)

r_li = []
for x in li:
    k_x = x_point - x[0]
    k_y = y_point - x[1]
    k_x *= k_x
    k_y *= k_y
    r_li.append(math.sqrt(k_x + k_y))

print(x_point, y_point, max(r_li))

# 딱봐도 이건 좀 아닌거 앎. 많이 잘못됨. 나중에함.