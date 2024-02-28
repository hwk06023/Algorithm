import sys

input = sys.stdin.readline

L = int(input())
S = list(map(int, input().split()))
n = int(input())
len_s = len(S)

if n < len_s:
    for i in range(n):
        print(S[i], end=' ')
    print()
else:
    term_list = [[1, S[0]-1]]
    for i in range(1, len_s):
        term_list.append([S[i-1]+1, S[i]-1])
    term_list.sort(key=lambda x: x[1]-x[0])
    print(term_list)
    result = list(S)
    tmp = n - len_s
    while tmp > 0:
        for i in range(len(term_list)):
            for j in range(2):
                if term_list[i][j] not in result:
                    result.append(term_list[i][j])
                    tmp -= 1
                if tmp == 0:
                    break
                term_list[i][j] += 1

print(result)