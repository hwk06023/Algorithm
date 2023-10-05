import sys

input = sys.stdin.readline

n = int(input())
li_int = list(map(int, input().split()))

if sum(li_int) == 0:
    print(0)
elif n == 1:
    print(li_int[0])
else:
    li_str = list(map(str, li_int))
    li_constr = list(map(str, li_int))
    tmp_len = []
    for i in range(n):
        tmp_len.append(len(li_str[i]))
    max_len = max(tmp_len)
    tmp_li = []
    for i in range(n):
        while(len(li_str[i]) < max_len):
            li_str[i] += li_str[i][:max_len-len(li_str[i])]
        tmp_li.append([li_int[i] // 10**(tmp_len[i]-1), tmp_len[i], int(li_str[i]), li_constr[i]])
    tmp_li.sort(key=lambda x: (x[0], x[2], -x[1]), reverse=True)

    li = [tmp_li[0][3]]
    for i in range(1, n):
        li.append(tmp_li[i][3])
        for j in range(i):
            if li[i] + li[j] > li[j] + li[i]:
                tmp_str = li[i]
                li[i] = li[j]
                li[j] = tmp_str
                break
    print(''.join(li))
