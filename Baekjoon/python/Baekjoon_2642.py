li = []
temp_li = []

for i in range(6):
    temp_li.append(list(map(int, input().split())))

all_zero = [0, 0, 0, 0, 0, 0]
ver_1 = [temp_li[0][0], temp_li[1][0], temp_li[2][0], temp_li[3][0], temp_li[4][0], temp_li[5][0]]
ver_2 = [temp_li[0][1], temp_li[1][1], temp_li[2][1], temp_li[3][1], temp_li[4][1], temp_li[5][1]]
ver_3 = [temp_li[0][2], temp_li[1][2], temp_li[2][2], temp_li[3][2], temp_li[4][2], temp_li[5][2]]
ver_4 = [temp_li[0][3], temp_li[1][3], temp_li[2][3], temp_li[3][3], temp_li[4][3], temp_li[5][3]]
ver_5 = [temp_li[0][4], temp_li[1][4], temp_li[2][4], temp_li[3][4], temp_li[4][4], temp_li[5][4]]
ver_6 = [temp_li[0][5], temp_li[1][5], temp_li[2][5], temp_li[3][5], temp_li[4][5], temp_li[5][5]]

if temp_li[0] != all_zero and temp_li[1] == all_zero: print(0)
elif temp_li[0] == all_zero and temp_li[1] != all_zero and temp_li[2] == all_zero: print(0)
elif temp_li[1] == all_zero and temp_li[2] != all_zero and temp_li[3] == all_zero: print(0)
elif temp_li[2] == all_zero and temp_li[3] != all_zero and temp_li[4] == all_zero: print(0)
elif temp_li[3] == all_zero and temp_li[4] != all_zero and temp_li[5] == all_zero: print(0)
elif temp_li[5] != all_zero and temp_li[4] == all_zero: print(0)
elif ver_1 != all_zero and ver_2 == all_zero: print(0)
elif ver_1 == all_zero and ver_2 != all_zero and ver_3 == all_zero: print(0)
elif ver_2 == all_zero and ver_3 != all_zero and ver_4 == all_zero: print(0)
elif ver_3 == all_zero and ver_4 != all_zero and ver_5 == all_zero: print(0)
elif ver_4 == all_zero and ver_5 != all_zero and ver_6 == all_zero: print(0)
elif ver_6 != all_zero and ver_5 == all_zero : print(0)
else:
    for i in range(6):
        if temp_li[i] != all_zero:
            li.append(temp_li[i])

    if len(li) == 2:
        i == 5
        while(i >= 0):
            if li[0][i] == 0 and li[1][i] == 0:
                del li[0][i]
                del li[1][i]
            i -= 1
        
        if len(li[0]) == 5:
            m_1 = li[0][0]
            m_2 = li[0][1]
            m_3 = li[0][2]
            m_4 = li[0][3]
            m_5 = li[0][4]
            m_6 = li[1][0]
            m_7 = li[1][1]
            m_8 = li[1][2]
            m_9 = li[1][3]
            m_10 = li[1][4]

            if m_1 != 0 and m_2 != 0 and m_3 != 0 and m_4 == 0 and m_5 == 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 != 0 and m_10 != 0:
                if m_1 == 1: print(m_3)
                elif m_2 == 1: print(m_9)
                elif m_3 == 1: print(m_1)
                elif m_8 == 1: print(m_10)
                elif m_9 == 1: print(m_2)
                elif m_10 == 1: print(m_8)
            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 != 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0:
                if m_3 == 1: print(m_5)
                elif m_4 == 1: print(m_7)
                elif m_5 == 1: print(m_3)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_4)
                elif m_8 == 1: print(m_6)
            else:
                print(0)
        else:
            print(0)

    elif len(li) == 3:
        i == 5
        while(i >= 0):
            if li[0][i] == 0 and li[1][i] == 0 and li[2][i] == 0:
                del li[0][i]
                del li[1][i]
                del li[2][i]
            i -= 1
        
        if len(li[0]) == 4:
            m_1 = li[0][0]
            m_2 = li[0][1]
            m_3 = li[0][2]
            m_4 = li[0][3]
            m_5 = li[1][0]
            m_6 = li[1][1]
            m_7 = li[1][2]
            m_8 = li[1][3]
            m_9 = li[2][0]
            m_10 = li[2][1]
            m_11 = li[2][2]
            m_12 = li[2][3]

            # case_1
            if m_1 != 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 == 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_1 == 1: print(m_7)
                elif m_2 == 1: print(m_10)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_1)
                elif m_8 == 1: print(m_6)
                elif m_10 == 1: print(m_2)
            elif m_1 != 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 == 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_1 == 1: print(m_7)
                elif m_2 == 1: print(m_11)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_1)
                elif m_8 == 1: print(m_6)
                elif m_11 == 1: print(m_2)
            elif m_1 != 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 == 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 == 0 and m_12 != 0:
                if m_1 == 1: print(m_7)
                elif m_2 == 1: print(m_12)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_1)
                elif m_8 == 1: print(m_6)
                elif m_12 == 1: print(m_2)

            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 != 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 == 0 and m_9 != 0 and m_10 == 0 and m_11 == 0 and m_12 == 0:
                if m_4 == 1: print(m_6)
                elif m_3 == 1: print(m_9)
                elif m_5 == 1: print(m_7)
                elif m_7 == 1: print(m_5)
                elif m_6 == 1: print(m_4)
                elif m_9 == 1: print(m_3)
            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 != 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 == 0 and m_9 == 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_4 == 1: print(m_6)
                elif m_3 == 1: print(m_10)
                elif m_5 == 1: print(m_7)
                elif m_7 == 1: print(m_5)
                elif m_6 == 1: print(m_4)
                elif m_10 == 1: print(m_3)
            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 != 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 == 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_4 == 1: print(m_6)
                elif m_3 == 1: print(m_11)
                elif m_5 == 1: print(m_7)
                elif m_7 == 1: print(m_5)
                elif m_6 == 1: print(m_4)
                elif m_11 == 1: print(m_3)

            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 == 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 != 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_2 == 1: print(m_10)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_9)
                elif m_8 == 1: print(m_6)
                elif m_9 == 1: print(m_7)
                elif m_10 == 1: print(m_2)
            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 == 0 and m_5 == 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 != 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_3 == 1: print(m_10)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_9)
                elif m_8 == 1: print(m_6)
                elif m_9 == 1: print(m_7)
                elif m_10 == 1: print(m_3)
            elif m_1 == 0 and m_2 == 0 and m_3 == 0 and m_4 != 0 and m_5 == 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 != 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_4 == 1: print(m_10)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_9)
                elif m_8 == 1: print(m_6)
                elif m_9 == 1: print(m_7)
                elif m_10 == 1: print(m_4)

            elif m_1 != 0 and m_2 == 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 == 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 != 0:
                if m_1 == 1: print(m_11)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_12)
                elif m_7 == 1: print(m_5)
                elif m_11 == 1: print(m_1)
                elif m_12 == 1: print(m_6)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 == 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 != 0:
                if m_2 == 1: print(m_11)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_12)
                elif m_7 == 1: print(m_5)
                elif m_11 == 1: print(m_2)
                elif m_12 == 1: print(m_6)
            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 == 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 != 0:
                if m_3 == 1: print(m_11)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_12)
                elif m_7 == 1: print(m_5)
                elif m_11 == 1: print(m_3)
                elif m_12 == 1: print(m_6)

            # case_2
            elif m_1 != 0 and m_2 == 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 != 0 and m_10 == 0 and m_11 == 0 and m_12 == 0:
                if m_1 == 1: print(m_9)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_9 == 1: print(m_1)
            elif m_1 != 0 and m_2 == 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_1 == 1: print(m_10)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_10 == 1: print(m_1)
            elif m_1 != 0 and m_2 == 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_1 == 1: print(m_11)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_11 == 1: print(m_1)
            elif m_1 != 0 and m_2 == 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 == 0 and m_12 != 0:
                if m_1 == 1: print(m_12)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_12 == 1: print(m_1)

            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 != 0 and m_10 == 0 and m_11 == 0 and m_12 == 0:
                if m_2 == 1: print(m_9)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_9 == 1: print(m_2)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_2 == 1: print(m_10)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_10 == 1: print(m_2)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_2 == 1: print(m_11)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_11 == 1: print(m_2)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 == 0 and m_12 != 0:
                if m_2 == 1: print(m_12)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_12 == 1: print(m_2)

            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 != 0 and m_10 == 0 and m_11 == 0 and m_12 == 0:
                if m_3 == 1: print(m_9)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_9 == 1: print(m_3)
            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_3 == 1: print(m_10)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_10 == 1: print(m_3)
            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_3 == 1: print(m_11)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_11 == 1: print(m_3)
            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 == 0 and m_12 != 0:
                if m_3 == 1: print(m_12)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_12 == 1: print(m_3)

            elif m_1 == 0 and m_2 == 0 and m_3 == 0 and m_4 != 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 != 0 and m_10 == 0 and m_11 == 0 and m_12 == 0:
                if m_4 == 1: print(m_9)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_9 == 1: print(m_4)
            elif m_1 == 0 and m_2 == 0 and m_3 == 0 and m_4 != 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_4 == 1: print(m_10)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_10 == 1: print(m_4)
            elif m_1 == 0 and m_2 == 0 and m_3 == 0 and m_4 != 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_4 == 1: print(m_11)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_11 == 1: print(m_4) 
            elif m_1 == 0 and m_2 == 0 and m_3 == 0 and m_4 != 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 == 0 and m_12 != 0:
                if m_4 == 1: print(m_12)
                elif m_5 == 1: print(m_7)
                elif m_6 == 1: print(m_8)
                elif m_7 == 1: print(m_5)
                elif m_8 == 1: print(m_6)
                elif m_12 == 1: print(m_4)

            # case_3
            elif m_1 != 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 == 0 and m_6 != 0 and m_7 != 0 and m_8 == 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 != 0:
                if m_1 == 1: print(m_7)
                elif m_2 == 1: print(m_11)
                elif m_6 == 1: print(m_12)
                elif m_7 == 1: print(m_1)
                elif m_11 == 1: print(m_2)
                elif m_12 == 1: print(m_6)
            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 != 0 and m_5 == 0 and m_6 != 0 and m_7 != 0 and m_8 == 0 and m_9 != 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_3 == 1: print(m_10)
                elif m_4 == 1: print(m_6)
                elif m_6 == 1: print(m_4)
                elif m_7 == 1: print(m_9)
                elif m_10 == 1: print(m_3)
                elif m_9 == 1: print(m_7)
        else:
            print(0)

    elif len(li) == 4:
        i == 5
        while(i >= 0):
            if li[0][i] == 0 and li[1][i] == 0 and li[2][i] == 0 and li[3][i] == 0:
                del li[0][i]
                del li[1][i]
                del li[2][i]
                del li[3][i]
            i -= 1    
        if len(li[0]) == 3:
            m_1 = li[0][0]
            m_2 = li[0][1]
            m_3 = li[0][2]
            m_4 = li[1][0]
            m_5 = li[1][1]
            m_6 = li[1][2]
            m_7 = li[2][0]
            m_8 = li[2][1]
            m_9 = li[2][2]
            m_10 = li[3][0]
            m_11 = li[3][1]
            m_12 = li[3][2]
            # case_1
            if m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 != 0 and m_5 != 0 and m_6 != 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_3 == 1: print(m_8)
                elif m_4 == 1: print(m_6)
                elif m_5 == 1: print(m_11)
                elif m_6 == 2: print(m_4)
                elif m_8 == 1: print(m_3)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_3 == 1: print(m_8)
                elif m_7 == 1: print(m_6)
                elif m_5 == 1: print(m_11)
                elif m_6 == 2: print(m_7)
                elif m_8 == 1: print(m_3)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 != 0 and m_11 != 0 and m_12 == 0:
                if m_3 == 1: print(m_8)
                elif m_10 == 1: print(m_6)
                elif m_5 == 1: print(m_11)
                elif m_6 == 2: print(m_10)
                elif m_8 == 1: print(m_3)
                elif m_11 == 1: print(m_5)

            elif m_1 != 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 != 0 and m_10 == 0 and m_11 == 0 and m_12 != 0:
                if m_1 == 1: print(m_9)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_12)
                elif m_8 == 1: print(m_2)
                elif m_9 == 1: print(m_1)
                elif m_12 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 != 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 != 0 and m_10 == 0 and m_11 == 0 and m_12 != 0:
                if m_4 == 1: print(m_9)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_12)
                elif m_8 == 1: print(m_2)
                elif m_9 == 1: print(m_4)
                elif m_12 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 == 0 and m_7 != 0 and m_8 != 0 and m_9 != 0 and m_10 == 0 and m_11 == 0 and m_12 != 0:
                if m_7 == 1: print(m_9)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_12)
                elif m_8 == 1: print(m_2)
                elif m_9 == 1: print(m_7)
                elif m_12 == 1: print(m_5)

            elif m_1 != 0 and m_2 == 0 and m_3 == 0 and m_4 != 0 and m_5 != 0 and m_6 != 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_1 == 1: print(m_8)
                elif m_4 == 1: print(m_6)
                elif m_5 == 1: print(m_11)
                elif m_6 == 1: print(m_4)
                elif m_8 == 1: print(m_1)
                elif m_11 == 1: print(m_5)
            elif m_1 != 0 and m_2 == 0 and m_3 == 0 and m_4 != 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 != 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_1 == 1: print(m_8)
                elif m_4 == 1: print(m_9)
                elif m_5 == 1: print(m_11)
                elif m_9 == 1: print(m_4)
                elif m_8 == 1: print(m_1)
                elif m_11 == 1: print(m_5)
            elif m_1 != 0 and m_2 == 0 and m_3 == 0 and m_4 != 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 != 0:
                if m_1 == 1: print(m_8)
                elif m_4 == 1: print(m_12)
                elif m_5 == 1: print(m_11)
                elif m_12 == 1: print(m_4)
                elif m_8 == 1: print(m_1)
                elif m_11 == 1: print(m_5)

            elif m_1 == 0 and m_2 != 0 and m_3 != 0 and m_4 == 0 and m_5 != 0 and m_6 == 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_2 == 1: print(m_8)
                elif m_3 == 1: print(m_7)
                elif m_5 == 1: print(m_10)
                elif m_7 == 1: print(m_3)
                elif m_8 == 1: print(m_2)
                elif m_10 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_2 == 1: print(m_8)
                elif m_6 == 1: print(m_7)
                elif m_5 == 1: print(m_10)
                elif m_7 == 1: print(m_6)
                elif m_8 == 1: print(m_2)
                elif m_10 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 == 0 and m_7 != 0 and m_8 != 0 and m_9 != 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_2 == 1: print(m_8)
                elif m_9 == 1: print(m_7)
                elif m_5 == 1: print(m_10)
                elif m_7 == 1: print(m_9)
                elif m_8 == 1: print(m_2)
                elif m_10 == 1: print(m_5)
            # case_2
            elif m_1 != 0 and m_2 != 0 and m_3 != 0 and m_4 == 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_1 == 1: print(m_3)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_3 == 1: print(m_1)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 != 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_1 == 1: print(m_6)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_3 == 1: print(m_1)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 != 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 != 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_1 == 1: print(m_9)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_9 == 1: print(m_1)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 != 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 != 0:
                if m_1 == 1: print(m_12)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_12 == 1: print(m_1)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 != 0 and m_4 != 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_4 == 1: print(m_3)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_3 == 1: print(m_4)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 != 0 and m_5 != 0 and m_6 != 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_4 == 1: print(m_6)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_6 == 1: print(m_4)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 != 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 != 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_4 == 1: print(m_9)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_9 == 1: print(m_4)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 != 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 != 0:
                if m_4 == 1: print(m_12)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_12 == 1: print(m_4)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 != 0 and m_4 == 0 and m_5 != 0 and m_6 == 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_7 == 1: print(m_3)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_3 == 1: print(m_7)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_7 == 1: print(m_6)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_6 == 1: print(m_7)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 == 0 and m_7 != 0 and m_8 != 0 and m_9 != 0 and m_10 == 0 and m_11 != 0 and m_12 == 0:
                if m_7 == 1: print(m_9)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_9 == 1: print(m_7)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 == 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 == 0 and m_11 != 0 and m_12 != 0:
                if m_7 == 1: print(m_12)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_12 == 1: print(m_7)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 != 0 and m_4 == 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 != 0 and m_11 != 0 and m_12 == 0:
                if m_10 == 1: print(m_3)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_3 == 1: print(m_10)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 != 0 and m_11 != 0 and m_12 == 0:
                if m_10 == 1: print(m_6)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_6 == 1: print(m_10)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 != 0 and m_10 != 0 and m_11 != 0 and m_12 == 0:
                if m_10 == 1: print(m_9)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_9 == 1: print(m_10)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 == 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 != 0 and m_11 != 0 and m_12 != 0:
                if m_10 == 1: print(m_12)
                elif m_2 == 1: print(m_8)
                elif m_5 == 1: print(m_11)
                elif m_12 == 1: print(m_10)
                elif m_8 == 1: print(m_2)
                elif m_11 == 1: print(m_5)
            # case_3
            elif m_1 != 0 and m_2 == 0 and m_3 == 0 and m_4 != 0 and m_5 != 0 and m_6 == 0 and m_7 == 0 and m_8 != 0 and m_9 != 0 and m_10 == 0 and m_11 == 0 and m_12 != 0:
                if m_1 == 1: print(m_8)
                elif m_4 == 1: print(m_9)
                elif m_5 == 1: print(m_12)
                elif m_8 == 1: print(m_1)
                elif m_9 == 1: print(m_4)
                elif m_12 == 1: print(m_5)
            elif m_1 == 0 and m_2 == 0 and m_3 != 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 != 0 and m_9 == 0 and m_10 != 0 and m_11 == 0 and m_12 == 0:
                if m_3 == 1: print(m_8)
                elif m_6 == 1: print(m_7)
                elif m_5 == 1: print(m_10)
                elif m_8 == 1: print(m_3)
                elif m_7 == 1: print(m_6)
                elif m_10 == 1: print(m_5)
        else:
            print(0)

    elif len(li) == 5:
        i == 5
        while(i >= 0):
            if li[0][i] == 0 and li[1][i] == 0 and li[2][i] == 0 and li[3][i] == 0 and li[4][i] == 0:
                del li[0][i]
                del li[1][i]
                del li[2][i]
                del li[3][i]
                del li[4][i]
            i -= 1

            if len(li[0]) == 2:
                m_1 = li[0][0]
                m_2 = li[0][1]
                m_3 = li[1][0]
                m_4 = li[1][1]
                m_5 = li[2][0]
                m_6 = li[2][1]
                m_7 = li[3][0]
                m_8 = li[3][1]
                m_9 = li[4][0]
                m_10 = li[4][1]
                if m_1 != 0 and m_2 == 0 and m_3 != 0 and m_4 == 0 and m_5 != 0 and m_6 != 0 and m_7 == 0 and m_8 != 0 and m_9 == 0 and m_10 != 0:
                    if m_1 == 1: print(m_5)
                    elif m_3 == 1: print(m_8)
                    elif m_5 == 1: print(m_1)
                    elif m_6 == 1: print(m_10)
                    elif m_8 == 1: print(m_3)
                    elif m_10 == 1: print(m_6)
                elif m_1 == 0 and m_2 != 0 and m_3 == 0 and m_4 != 0 and m_5 != 0 and m_6 != 0 and m_7 != 0 and m_8 == 0 and m_9 != 0 and m_10 == 0:
                    if m_2 == 1: print(m_6)
                    elif m_4 == 1: print(m_7)
                    elif m_5 == 1: print(m_9)
                    elif m_6 == 1: print(m_2)
                    elif m_7 == 1: print(m_4)
                    elif m_9 == 1: print(m_5)
                else:
                    print(0)
            else:
                print(0)
    
    else:
        print(0)
