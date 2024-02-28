import sys

input = sys.stdin.readline

dict_li = []
while True:
    word = input().rstrip()
    if word == '-':
        break
    dict_li.append(word)
    
ex_li = []
while True:
    word = input().rstrip()
    if word == '#':
        break
    ex_li.append(word)

for ex_word in ex_li:
    flag = {}
    for ex_char in list(ex_word):
        flag[ex_char] = 0
        for dict_word in dict_li:
            if ex_char in list(dict_word):
                bool = True
                for l in dict_word:
                    if dict_word.count(l) > ex_word.count(l):
                        bool = False
                        break
                if bool:
                    flag[ex_char] += 1
    min_li = []      
    max_li = []          
    for x in flag:
        if flag[x] == min(flag.values()):
            min_li.append(x)
        if flag[x] == max(flag.values()):
            max_li.append(x)
    min_li.sort()
    max_li.sort()
    print("".join(min_li), min(flag.values()), "".join(max_li), max(flag.values()))
