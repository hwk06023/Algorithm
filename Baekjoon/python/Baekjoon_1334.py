n = input()

if len(n) == 1:
    if n == '9':
        print(11)
    else:
        print(int(n) + 1)
else:
    if set(n) == {'9'}: # 9999..
        print(int(n) + 2)
    else:
        if len(n) % 2 == 0:
            a = n[:len(n)//2] # 12
            a_reverse = a[::-1] # 21
            b = n[len(n)//2:] # 34

            if int(a_reverse) > int(b): # 21 > 34
                print(a + a_reverse)
            elif int(a_reverse) == int(b): # 21 == 34 100 001
                a = str(int(a) + 1)
                a_reverse = a[::-1]
                print(a + a[::-1])
            else:
                a = str(int(a) + 1)
                a_reverse = a[::-1]
                print(a + a[::-1])

        else:
            a = n[:len(n)//2] # 12
            a_reverse = a[::-1] # 21
            mid = n[len(n)//2] # 3
            b = n[len(n)//2+1:] # 45

            if int(a_reverse) > int(b): # 21 > 45
                print(a + mid + a_reverse)
            else:
                if mid == '9':
                    a = str(int(a) + 1)
                    a_reverse = a[::-1]
                    print(a + '0' + a[::-1])
                else:
                    print(a + str(int(mid) + 1) + a_reverse)
                
