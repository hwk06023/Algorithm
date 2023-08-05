n = int(input())
li = list(map(int, input().split()))

if n == 1:
    print(li[0])
elif n == 2:
    flag = sum(li)
    print(max(flag, flag-li[0], flag-li[1]))
else:
    flag_li_1 = [li[0]]
    flag_li_2 = [-9999999999]
    flag = li[0]

    for i in range(1, n):
        flag_li_2.append(max(flag_li_1[-1], flag_li_2[-1]+li[i]))
        flag_li_1.append(max(li[i], flag_li_1[-1]+li[i]))
        flag = max(flag, flag_li_1[i], flag_li_2[i])

    print(flag)