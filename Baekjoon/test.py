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
'''

