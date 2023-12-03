import sys

input = sys.stdin.readline

n = int(input())

oh_li = ['(', ')', '[', ']', '{', '}', '.', ',' , ';', ':', ' ']

for k in range(n):
    str1_li = list(input().lower().rstrip())
    str2_li = list(input().lower().rstrip())
    
    for i in range(len(str1_li)-1, -1, -1):
        if str1_li[i] == ' ' and (i==len(str1_li)-1 or str1_li[i-1] in oh_li or str1_li[i+1] in oh_li):
            del str1_li[i]
        elif str1_li[i] == '{' or str1_li[i] == '[':
            str1_li[i] = '('
        elif str1_li[i] == '}' or str1_li[i] == ']':
            str1_li[i] = ')'
        elif str1_li[i] == ';':
            str1_li[i] = ','
    
    for i in range(len(str2_li)-1, -1, -1):
        if str2_li[i] == ' ' and (i==len(str2_li)-1 or str2_li[i-1] in oh_li or str2_li[i+1] in oh_li):
            del str2_li[i]
        elif str2_li[i] == '{' or str2_li[i] == '[':
            str2_li[i] = '('
        elif str2_li[i] == '}' or str2_li[i] == ']':
            str2_li[i] = ')'
        elif str2_li[i] == ';':
            str2_li[i] = ','
    
    if str1_li[0] == ' ':
        del str1_li[0]
    if str2_li[0] == ' ':
        del str2_li[0]


    if str1_li == str2_li:
        print('Data Set '+str(k+1)+': equal')
    else:
        print('Data Set '+str(k+1)+': not equal')
    
    if k != n-1:
        print()