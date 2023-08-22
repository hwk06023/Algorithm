n = list(input())

li = [0] * 10
z_tmp = 0
for i in range(len(n)-1, -1, -1):
    k = len(n) - i
    tmp = int(n[i]) 
    if tmp == 0:
        z_tmp += 1
    else:    
        digit = 10 ** (k-1)
        all_tmp = (k-1) * digit//10
        
        for j in range(1, 10):
            li[j] += all_tmp*tmp
        
        for j in range(1, tmp):
            li[j] += digit

        li[tmp] += 1
        for x in n[:-k]:
            x = int(x)
            li[x] += tmp * digit

        if  k > 1 and tmp > 0:
            li[0] += ((digit//10) + 1)*(k-1) - int('1'*(k-1)) + ((tmp-1)*(k-1))*(digit//10)
        if z_tmp == 0:
            for z in range(1, k-1):
                li[0] += (9 * (10 ** (k-2-z))) * z
        else:
            for z in range(1, k-1-z_tmp):
                li[0] += (9 * (10 ** (k-2-z_tmp-z))) * z
            z_tmp = 0

print(' '.join(map(str, li)))
