import sys

input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

n1 = len(str1)
n2 = len(str2)

lcs = [[0] * n1 for _ in range(n2)]
str_lcs = ""

for i in range(n2):
    for j in range(n1):
        if str2[i] == str1[j]:
            if i == 0 or j == 0:
                lcs[i][j] = 1
            else:
                lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            if i == 0 and j == 0:
                lcs[i][j] = 0
            elif i == 0:
                lcs[i][j] = lcs[i][j-1]
            elif j == 0:
                lcs[i][j] = lcs[i-1][j]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[n2-1][n1-1])

n1 -= 1
n2 -= 1

while n1 >= 0 and n2 >= 0:
    if str2[n2] == str1[n1]:
        str_lcs = str2[n2] + str_lcs
        n2 -= 1
        n1 -= 1
    else:
        if n2 == 0:
            n1 -= 1
        elif n1 == 0:
            n2 -= 1
        else:
            if lcs[n2-1][n1] > lcs[n2][n1-1]:
                n2 -= 1
            else:
                n1 -= 1

print(str_lcs)