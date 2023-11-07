n = int(input())
li = list(map(int, input().split()))
flag_li = []

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def is_flag(li):
    for i in range(1, n):
        if  is_prime(li[0] + li[i]):
            print('if',li[i], i)
            tmp_li = li[1:i] + li[i+1:]
            print('tmp_li', len(tmp_li), tmp_li)
            if len(tmp_li) == 0:
                print('append',li[i])
                flag_li.append(li[i])
                break
            is_flag(tmp_li)
        else:
            print('else',li[i], i)
            break
            
        
is_flag(li)
if len(flag_li) == 0:
    print(-1)
else:
    flag_li.sort()
    print(''.join(map(str, flag_li)))


