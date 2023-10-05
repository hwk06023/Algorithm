import sys
from itertools import combinations

input = sys.stdin.readline

while(1):
    n = int(input())
    if(n == 0):
        break
    elif(n == 3):
        li = []
        for _ in range(n):
            li.append(int(input()))
        li = sorted(li)

        print(li[n-1]-li[n-3] + li[n-2]-li[n-3])
     
    elif(n == 4):
        li = []
        for _ in range(n):
            li.append(int(input()))
        li = sorted(li)

        print(li[n-1]-li[n-4] + li[n-2]-li[n-4] + li[n-3]-li[n-4])  
    
    elif(n % 2 == 0): # 대척점 존재
        li = [0] * n
        flag_li = set()
        range_li = []

        for i in range(n):
            temp = int(input())
            li[i] = temp
            li.append(temp)
            range_li.append(list(range(i, i + n//2 + 1)))
        
        for i in range(len(range_li)):
            for j in range(n//2+1):
                if range_li[i][j] >= n:
                    range_li[i][j] -= n

        all_comb_3 = list(combinations(list(range(n)), 3))
        all_comb_4 = list(combinations(list(range(n)), 4))
        reverse_li = set()
        for x in all_comb_3:
            for k in range_li:
                if x[0] in k and x[1] in k and x[2] in k:
                    reverse_li.add((x))

        comb = list(set(all_comb_3) - reverse_li)
        comb_li_3 = []
        comb_li_4 = []

        for x in comb:
            if abs(x[0] - x[1]) == n//2 or abs(x[0] - x[2]) == n//2 or abs(x[2] - x[1]) == n//2:
                continue
            else:
                comb_li_3.append(x)
               
        for x in comb_li_3:
            flag_temp = 0
            for i in range(n):
                if li[i] > min(li[x[0]], li[x[1]], li[x[2]]):
                    flag_temp += li[i] - min(li[x[0]], li[x[1]], li[x[2]])
            flag_li.add(flag_temp)

        for x in all_comb_4:
            if abs(x[0] - x[1]) == n//2 and abs(x[2] - x[3]) == n//2:
                comb_li_4.append(x)
            elif abs(x[0] - x[2]) == n//2 and abs(x[1] - x[3]) == n//2:
                comb_li_4.append(x)
            elif abs(x[0] - x[3]) == n//2 and abs(x[1] - x[2]) == n//2:
                comb_li_4.append(x)
        
        for x in comb_li_4:
            flag_temp = 0
            for i in range(n):
                if li[i] > min(li[x[0]], li[x[1]], li[x[2]], li[x[3]]):
                    flag_temp += li[i] - min(li[x[0]], li[x[1]], li[x[2]], li[x[3]])
            flag_li.add(flag_temp)
        
        print(min(flag_li))

    else: # 대척점 존재 X 
        li = [0] * n
        flag_li = set()
        range_li = []

        for i in range(n):
            temp = int(input())
            li[i] = temp
            li.append(temp)
            range_li.append(list(range(i, i + (n+1)//2)))
        
        for i in range(len(range_li)):
            for j in range((n+1)//2):
                if range_li[i][j] >= n:
                    range_li[i][j] -= n

        all_comb = list(combinations(list(range(n)), 3))
        reverse_li = set()
        for x in all_comb:
            for k in range_li:
                if x[0] in k and x[1] in k and x[2] in k:
                    reverse_li.add((x))
        
        comb_li = list(set(all_comb) - reverse_li)
        
        for x in comb_li:
            flag_temp = 0
            for i in range(n):
                if li[i] > min(li[x[0]], li[x[1]], li[x[2]]):
                    flag_temp += li[i] - min(li[x[0]], li[x[1]], li[x[2]])
            flag_li.add(flag_temp)
        
        print(min(flag_li))
        
    print()
    