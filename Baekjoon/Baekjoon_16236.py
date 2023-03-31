n = int(input())

li = [[]] * n

for i in range(n):
    li[i] = list(map(int, input().split()))
    if 9 in li[i]:
        for j in range(n):
            if li[i][j] == 9:
                x, y = j, i

state = 2
flag = 0

while(1):
    temp = 0
    temp_dict = {}
    check_cnt = 0

    for i in range(n):
        for j in range(n):
            if li[i][j] < state and li[i][j] > 0 and li[i][j] < 7:
                if x > j:
                    temp += x - j
                    if y > i:
                        temp += y - i
                    else:
                        temp += i - y
                else:
                    temp += j - x
                    if y > i:
                        temp += y - i
                    else:
                        temp += i - y
            else:
                check_cnt += 1
            if(temp > 0): 
                temp_li[temp] = [i, j]

    if check_cnt == n*n: break
    
    state += 1
    flag += min(temp_li)

    min_temp = 99
    min_i = 0

    for i in range(len(temp_li)):
        if temp_li[i] < min_temp:
            min_temp = temp_li[i]
            min_i = i
    print(li)

    li[temp_xy[min_i][1]][temp_xy[min_i][0]] = 0
        

print(flag)