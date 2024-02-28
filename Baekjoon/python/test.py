'''
n = int(input())
li = []

for i in range(n):
    li_in = list(input().split())
    if li_in[0] == 'add' and li_in[1] not in li: 
        li.append(li_in[1])
    elif li_in[0] == 'check':
        if li_in[1] in li: print('1')
        else: print('0')
    elif li_in[0] == 'remove' and li_in[1] in li: 
        li.remove(li_in[1])
    elif li_in[0] == 'toggle':
        if li_in[1] in li: 
            li.remove(li_in[1])
        else: 
            li.append(li_in[1])
    elif li_in[0] == 'all':
        li = ['1', '2', '3', '4', '5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    else: 
        li = []
import sys

n = int(sys.stdin.readline())
li = set()

for i in range(n):
    li_in = list(sys.stdin.readline().strip().split())

    if li_in[0] == "add":
        li.add(int(li_in[1]))
    elif li_in[0] == "remove":
        li.discard(int(li_in[1]))
    elif li_in[0] == "check":
        if int(li_in[1]) in li: print('1')
        else: print('0')
    elif li_in[0] == "toggle":
        if int(li_in[1]) in li:
            li.discard(int(li_in[1]))
        else:
            li.add(int(li_in[1]))
    elif li_in[0] == "all":
        li = set(range(1, 21))
    else:
        li = set()

#-------------------------

n = int(input())
li_a = sorted(list(map(int, input().split())))
li_b = sorted(list(map(int, input().split())), reverse=True)

flag = 0

for i in range(n):
    flag += li_a[i]*li_b[i]
print(flag)

#-------------------------

n = int(input())
li = []
alpha_li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u','v','w','x','y','z']

for _ in range(n):
    li.append(input())
for x in li:
    if 'lol' in x:
        print(0)
    elif ('lo' in x) or ('ol' in x) or ('ll' in x):
        print(1)
    elif ('l' in x) or ('o' in x):
        if any('l' + alpha + 'l' in x for alpha in alpha_li):   print(1)
        else:    print(2)
    else:
        print(3)

#---------------------

n = int(input())
m = int(input())

dur = True
virus = [1]
li = []

for _ in range(m):
    li.append(list(map(int, input().split())))

while(dur):
    dur = False
    for i in virus:
        for x in li:
            if i == x[0] and x[1] not in virus:
                virus.append(x[1])
                dur = True
            elif i == x[1] and x[0] not in virus:
                virus.append(x[0])
                dur=True

print(len(virus)-1)

#---------------------아래 시간초과레전드

n = int(input())
m = int(input())
s = input()

temp = 0
flag_cnt = 0

for i in range(m-1, 3, -1):
    if s[i] == 'I':
        if n > 1:
            temp = 0
            for j in range(n):
                if s[i-1-(j*2)] == 'O' and s[i-2-(j*2)] == 'I': 
                    temp += 1
            if temp == n:
                flag_cnt += 1

        else:
            if s[i-1] == 'O' and s[i-2] == 'I':
                flag_cnt += 1

print(flag_cnt)

#------------ 아래는 50점짜리 코드 킹받네요

n = int(input())
m = int(input())
s = input()

flag_IOI = 'IOI' + ('OI' * (n-1))
flag_cnt = 0

for i in range(m - (2*n) + 2):
    if s[i:i+(2*n+1)] == flag_IOI:
        flag_cnt += 1

print(flag_cnt)

#---------------------------

n = int(input())
m = int(input())
s = input()

flag_IOI = 'IOI' + ('OI' * (n-1))
flag_cnt = 0

i = 0
while(i < m - (2*n) + 2):
    j = i+(2*n+1)
    if s[i:j] == flag_IOI:
        flag_cnt += 1
        while(j+1 <= m-1):
            if s[j] == 'O' and s[j+1] == 'I':
                flag_cnt += 1
                j+=2
            else:
                break
        i=j
    else:
        i += 1
print(flag_cnt)

import sys

m, n = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))
sum_li = [0]
sum_temp = 0

for i in range(m):
    sum_temp += li[i]
    sum_li.append(sum_temp)

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(sum_li[b]-sum_li[a-1])

n = int(input())
tmp = 1

for i in range(1, 19000):
    if (n == 1):
        print(1)
        break
    elif(tmp < n and n <= (tmp + 6*i)):
        print(i+1)
        break
    tmp += 6*i

from itertools import permutations
n, m = map(int, input().split())

li = list(permutations(list(range(1,n+1)), m))
flag_li = []

if(m == 1):
    for i in range(1,n+1):
        print(i)
else:
    for x in li:
        cnt = 0
        for i in range(m-1):
            if x[i] < x[i+1]:
                cnt += 1
        if cnt == m-1:
            flag_li.append(x)

    for x in flag_li:
        for i in range(m-1):
            print(x[i],end=' ')
        print(x[m-1])

#---------------------------------
]
import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
li = [0] * n

for i in range(n):
    li[i] = int(input())
li.sort()

flag_li = set()
m_dict = dict(Counter(li))
max_d = max(m_dict.values())
for i in range(n):
    if m_dict[li[i]] == max_d:
        flag_li.add(li[i])

flag_li = sorted(flag_li)


print(round(sum(li) / n))
print(li[(n-1) // 2])

if len(flag_li) == 1:
    print(flag_li[0])
else:
    print(flag_li[1])
print(max(li) - min(li))

#######################----------------

import sys

input = sys.stdin.readline
n, m, b = map(int, input().split())

li = []

for i in range(n):
    li.append(list(map(int, input().split())))

time = 1000000000000000
layer = 0

for now_layer in range(0, 257):
    temp_b = b
    time_temp = 0
    for i in range(n):
        for j in range(m):
            tmp = li[i][j] - now_layer
            if li[i][j] > now_layer:
                temp_b += tmp
                time_temp += 2 * tmp
            else:
                temp_b -= -1 * tmp
                time_temp += -1 * tmp
            
    if temp_b >= 0:
        if time >= time_temp:
                time = time_temp
                layer = now_layer

print(time, layer)
 
#-----------------------------------------

import sys

input = sys.stdin.readline

while(True):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)

    if a==0 and b==0 and c==0:
        break

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("right")
    else:
        print("wrong")

#------------------------------------------------

import sys

input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

li = sorted(li)

for x in li:
    print(x[0], x[1])

#-------------------------------------------

import sys

input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

li = sorted(li)

for x in li:
    print(x)

#-------------------------------

import sys

input = sys.stdin.readline

n = int(input())

check_list = [0] * 10001

for _ in range(n):
    k = int(input())
    
    check_list[k] += 1
    
for i in range(1, 10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)

#------------------------------------------

import sys

input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    li.append(list(map(int, input().split())))


li.append(li[0])

sum_1 = 0
sum_2 = 0
for i in range(n):
    sum_1 += li[i][0]*li[i+1][1]
    sum_2 += li[i][1]*li[i+1][0]

print(round(abs((sum_1 - sum_2)/2), 1))


def CCW(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y):
    ccw = (p2_x-p1_x)*(p3_y-p1_y)-(p3_x-p1_x)*(p2_y-p1_y)
    if ccw:
        ccw //= abs(ccw)
    return ccw

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
ccw3 = CCW(x1, y1, x2, y2, x3, y3)
ccw4 = CCW(x1, y1, x2, y2, x4, y4)
ccw1 = CCW(x3, y3, x4, y4, x1, y1)
ccw2 = CCW(x3, y3, x4, y4, x2, y2)
if ccw1 * ccw2 == 1 or ccw3 * ccw4 == 1:
    print(0)
elif ccw1 == 0 and ccw2 == 0:
    if x1 == x2:
        if max(y1, y2) < min(y3, y4) or max(y3, y4) < min(y1, y2):
            print(0)
        elif max(y1, y2) == min(y3, y4):
            print(1)
            print(x1, max(y1, y2))
        elif max(y3, y4) == min(y1, y2):
            print(1)
            print(x1, min(y1, y2))
        else:
            print(1)
    else:
        if max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2):
            print(0)
        elif max(x1, x2) == min(x3, x4):
            print(1)
            if x1 > x2:
                print(x1, y1)
            else:
                print(x2, y2)
        elif max(x3, x4) == min(x1, x2):
            print(1)
            if x1 < x2:
                print(x1, y1)
            else:
                print(x2, y2)
        else:
            print(1)
else:
    print(1)
    if x1 == x2:
        a2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - a2 * x3
        print(x1, a2 * x1 + b2)
    elif x3 == x4:
        a1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - a1 * x1
        print(x3, a1 * x3 + b1)
    else:
        a1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - a1 * x1
        a2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - a2 * x3
        print((b2 - b1) / (a1 - a2), a1 * (b2 - b1) / (a1 - a2) + b1)

###############3

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

if k > n/2:
    k = n-k

s = n
t = k

if k == 0:
    print(1)
else:
    for i in range(1, k):
        s *= (n-i)
        t *= (k-i)

    print(s // t)

########~~~~~~~

import sys 

input = sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))

flag = 0
gcd = 0

if n == 1:
    flag = li[0]
elif n == 2 or n == 3:

else:
    tmp_li = li[0:n//2]
    while (1) { 
        a = max(tmp_li[0], tmp_li[1])
        b = min(tmp_li[0], tmp_li[1])
        while (1) {
            c = a % b
            a = b
            b = c

            if a % b == 0:
                del tmp_li[0]
                del tmp_li[1]
                tmp_li.append(b)
                break
        }

    }

print(flag)

######~~

n = int(input())

li = [0, 1]

for i in range(1, n):
    li.append(li[i] + li[i-1])

print(li[n])

##############


n = int(input())

li = [0] * 10
for i in range(1,n+1):
    tmp = str(i)
    for x in tmp:
        x = int(x)
        li[x] += 1

print(' '.join(map(str, li)))


'''

print(list(set([1,2,3]) - set([1,3])))  