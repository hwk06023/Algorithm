import sys

input = sys.stdin.readline

n = int(input())
li = [list(input().rstrip()) for _ in range(n)]

alpha_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0}
zero_possible_dict = {'A': True, 'B': True, 'C': True, 'D': True, 'E': True, 'F': True, 'G': True, 'H': True, 'I': True, 'J': True}

for i in range(n):
    for j in range(len(li[i])):
        if j == 0:
            zero_possible_dict[li[i][j]] = False
        alpha_dict[li[i][j]] += 10 ** (len(li[i]) - j - 1)

alpha_dict = sorted(alpha_dict.items(), key=lambda x: x[1])

for i in range(len(alpha_dict)):
    if zero_possible_dict[alpha_dict[i][0]]:
        del alpha_dict[i]
        break

flag = 0
for i in range(9):
    flag += alpha_dict[i][1] * (i+1)

print(flag)