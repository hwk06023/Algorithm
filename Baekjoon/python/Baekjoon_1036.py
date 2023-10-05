import sys

input = sys.stdin.readline

dict_36 = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F':15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 
            'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P':25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 
            'U': 30, 'V': 31, 'W':32, 'X': 33, 'Y': 34, 'Z': 35 }

for i in range(10):
    dict_36[str(i)] = i

n = int(input())

cnt = dict().fromkeys(dict_36.keys(), 0)

li = []
for _ in range(n):
    tmp = input().rstrip()
    for i in range(len(tmp)):
        cnt[tmp[i]] += (36**(len(tmp)-i-1)) * (35 - dict_36[tmp[i]])
    li.append(tmp)
k = int(input())

cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

for i in cnt[:k]:
    dict_36[i[0]] = 35

flag = 0
for i in range(n):
    tmp = 0
    for j in range(len(li[i])):
        tmp += dict_36[li[i][j]] * (36**(len(li[i])-j-1))
    flag += tmp

def make_36(flag):
    if flag == 0:
        return '0'
    else:
        tmp = ''
        while flag > 0:
            if flag % 36 < 10:  
                tmp += str(flag % 36)
            else:
                tmp += chr(flag % 36 + 55)
            flag //= 36
        return tmp[::-1]

print(make_36(flag))
